# Hypothes.is-2-Are.na
A way to move your Hypothes.is annotations to an Are.na Channel

[Hypothes.is](https://hypothes.is) handles the web annotation space quite well. Managing the annotations that you have, however, proves tricky.

[Are.na](https://are.na) is a great way to visually organize and connect information like pictures and text.

What I wanted to do was have a way to take annotations from an article and house them in an Are.na channel. That way I could visually organize and connect these annotations across resources.

This code is a by-product of that want. It is currently organized so that you make an Are.na channel of the annotations for a specific resource (blog post, article, pdf, etc).

### How to use

- Clone the repo.

- Put in your Hypothes.is and Are.na access tokens in the utils.py file. You can find these in your account from the developer sections from each.

- Pull up a Python console and get going! 

```
> from app import main

# Use the title provided by Hypothes.is as the argument
> main('Thought as a Technology')

# Check Are.na to see the results!
> 'See if it worked!'
```
