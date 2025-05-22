# 🐍 Python day03 Input and Escape Sequences Demo

This Python script demonstrates:

- Taking user input
- Basic string operations
- Type conversion
- String concatenation
- Extensive use of **escape sequence characters**

It’s ideal for beginners learning how Python handles strings and special characters.

---

## 📄 File: `escape_sequence_demo.py`

### 🧾 Features Covered

| Escape       | Name             | Description                                             | Example Output                            |
| ------------ | ---------------- | ------------------------------------------------------- | ----------------------------------------- |
| `\\`         | Backslash        | Inserts a backslash (`\`)                               | `Hello \\World` → `Hello \World`          |
| `\'`         | Single Quote     | Inserts a single quote                                  | `It\'s OK` → `It's OK`                    |
| `\"`         | Double Quote     | Inserts a double quote                                  | `He said \"Hello\"` → `He said "Hello"`   |
| `\n`         | Newline          | Moves to the next line                                  | `Hello\nWorld` → `Hello`<br>`World`       |
| `\t`         | Horizontal Tab   | Inserts a tab space                                     | `Hello\tWorld` → `Hello    World`         |
| `\r`         | Carriage Return  | Moves cursor to beginning of the line (overwrites text) | `Hello\rWorld` → `World`                  |
| `\b`         | Backspace        | Deletes the character before it                         | `Helloo\bWorld` → `HelloWorld`            |
| `\f`         | Form Feed        | New page feed (used in printing)                        | `Hello\fWorld` → Output depends on system |
| `\v`         | Vertical Tab     | Vertical space/tab                                      | `Hello\vWorld` → Output may vary          |
| `\a`         | Bell / Alert     | Triggers a system beep                                  | `Hello\aWorld` → System beep              |
| `\0`         | Null Character   | Represents null character                               | Used internally in strings                |
| `\ooo`       | Octal Value      | Character represented by octal number `ooo`             | `\101` → `A`                              |
| `\xhh`       | Hex Value        | Character represented by hexadecimal `hh`               | `\x41` → `A`                              |
| `\uXXXX`     | Unicode (16-bit) | Unicode character using 4-digit hex                     | `\u0041` → `A`                            |
| `\UXXXXXXXX` | Unicode (32-bit) | Unicode using 8-digit hex                               | `\U0001F600` → 😀                         |
| `\N{name}`   | Unicode by Name  | Unicode character by descriptive name                   | `\N{grinning face}` → 😀                  |


