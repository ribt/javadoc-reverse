# Reverse Javadoc

This is a very simple Python script to create empty Java files from the Javadoc. If you have a Javadoc of a library you need to code, it could be useful to create a good starting point.

## Usage

```
./ReverseJavadoc.py [-i chars] javadoc out_dir

  javadoc               location of the Javadoc (a file path or an URL)
  out_dir               location of the directory to store Java files
  -i, --indent-with     choose the indentation chars
```

The default indentation char is a tabulation.

### Example

```
./ReverseJavadoc.py ../Javadoc/ out/
```

or

```
./ReverseJavadoc.py -i "  " https://openjfx.io/javadoc/11/ out/
```

### Disclaimer

This tool is not complete at all (for instance annotations like @Override or @Deprecated are ignored). Feel free to make a PR to improve it :)

[The frenchie4111's project](https://github.com/frenchie4111/Reverse-Javadoc) is much more advanced but too old and it is not working anymore (and I'm too lazy to update it).

