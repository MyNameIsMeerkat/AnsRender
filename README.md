# AnsRender


A tiny Python script to render ANSI art (.ANS) files in the terminal.

Usage is super simple:

```
python AnsRender.py <file_to_view.ans>
```
Which will render out the image using the correct codepage 437 like below:

![image](https://raw.github.com/MyNameIsMeerkat/AnsRender/master/example.png)

The quality of the render will depend on the width of the terminal, 80 columns wide is generally recommended and you will get a warning if a different width terminal is detected.

Also the fixed width used in the terminal will also change how nicely the characters render. Courier New tends to do a reasonable job of making things look nice.

For this to work on MS Windows you will need to install the `colorama` module.

### Refs
Lots of examples of ANSI art from AAA in `.ans` format can be found here: [http://artscene.textfiles.com/ansi/](http://artscene.textfiles.com/ansi/)
