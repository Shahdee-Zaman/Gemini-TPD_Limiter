# Gemini-TPD_Limiter
A python based TPD (Token Per Day) limiter created using Redis. It is useful for managing rate limits, ensuring you stay within your tier's limit and avoind incurring extra charges.

## Features
- Redis for fast and accurate rate tracking
- Daily reset of token counter
- Automatically resets usage counter based on UTC date
- Easy to implement
- Accurate token counting made specifically for Google's Gemini

## Requirements
- Python
- Redis

## For Windows
Requires WSL(Windows Subsystem for Linux) or Docker for running Redis on Windows

## Usage Instruction
Gemini_call.py is not required and is simply an example to show how to call rtc.py and use it.

## License
MIT

