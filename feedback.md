# Feedback

- A lot of user input is mixed in with "business" logic (e.g. creating rarities, etc.)
  - It would be nice to see this separated out. Kind of like MVC, except instead of a view, you have the user's terminal as the "view".
- Creating a class or two to encapsulate shared logic would be nice.
  - Perhaps one class to handle all the terminal interaction and one class to handle generating the items.
- Instead of using a list to group shared data, create a class.
- No unit tests
- Using `global` often is not recommended and is an indication to refactor your code.
  - Instead of manipulating a `global` variable inside a function, consider:
    - Passing the variable to the function
    - Creating a class and refactoring your `global` variable to be a class property

## Recommended Further Reading
- https://www.freecodecamp.org/news/four-pillars-of-object-oriented-programming/
- https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/
