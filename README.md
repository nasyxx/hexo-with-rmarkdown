# hexo-with-rmarkdown
ssssss
## Before
To blogging with R, you should first install package 'rmarkdown'.
### a simple tutorial
```R
#language: R
install.packages('rmarkdown')
```

then render the `Rmd` file into `html` file.
```R
#language: R
render('[filename]')
```
for details: [here][link of rmarkdown]

## Start
### demo
render the `demo.html` file into hexo style file `demo.html.hexo.md`.
```python
python hexo-with-rmarkdown.py [filename]
```

more functions are under construction.

[link of rmarkdown]: https://github.com/rstudio/rmarkdown