# Strings

print("String", 'Another String '
      'He\'s Right ' # Escaping characters with the backspace (\)
      """ He's Right"""
      )

long_string = """Here's a new line:
...
... It's right there!"""

print(long_string)

# You can add strings together with plus sign
print(
    "string1 " + "string2"
)

# You can add and multiply strings, but you are not able to subtract or divide

status_message = "Hey we have {} people using the sight right now"
# The {} represent where we will put the value in our variable template
# we use the format method (str.format) to put the value inside our variable

print(status_message.format(39))
