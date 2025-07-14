import os
import google.generativeai as genai
import redis
from redis_token_counter import TPDLimit


# Multiple dbs used rather than ports to lower resource usage
flash = TPDLimit(host='localhost', port=6379, db=2, limit=900000)
lite = TPDLimit(host='localhost', port=6380, db=1, limit=900000)

# Multiple models can be created as long as the token count is not shared between the models.
first_model = genai.GenerativeModel('gemini-2.0-flash')
second_model = genai.GenerativeModel('gemini-2.0-flash-lite')


prompt = input("Ask any question.")

# Gemini counts the token from input and returns an integer
# total_tokens is required to receive an integer otherwise it will return an object 'CountTokensResponse'.
input_token = first_model.count_tokens(prompt).total_tokens

# Proceed only if there is enough tokens left
if flash.generate(input_token):
    response = first_model.generate_content(prompt)
    print(response.text)
    # Increment the response to Redis database. Gemini automatically does token count
    flash.response_count(response.usage_metadata.candidates_token_count)

# Different model called if the first model has reached the token limit
elif lite.generate(input_token):
    response = second_model.generate_content(prompt)
    print(response.text)
    # Response incremented for proper tracking
    lite.response_count(response.usage_metadata.candidates_token_count)



