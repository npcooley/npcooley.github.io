---
title: "Using SynExtend - Simple"
excerpt: "A simple workflow with SynExtend, simply using a synteny map to perform orthology inference between two genomes."
collection: portfolio
output:
  md_document:
    variant: gfm
    preserve_yaml: TRUE
knit: (function(inputFile, encoding) {
  rmarkdown::render(inputFile,
    encoding = encoding,
    output_dir = "../_portfolio") })
always_allow_html: true
---

## R Markdown

This is an R Markdown document. Markdown is a simple formatting syntax
for authoring HTML, PDF, and MS Word documents. For more details on
using R Markdown see <http://rmarkdown.rstudio.com>.

When you click the **Knit** button a document will be generated that
includes both content as well as the output of any embedded R code
chunks within the document. You can embed an R code chunk like this:

``` r
summary(cars)
```

    ##      speed           dist       
    ##  Min.   : 4.0   Min.   :  2.00  
    ##  1st Qu.:12.0   1st Qu.: 26.00  
    ##  Median :15.0   Median : 36.00  
    ##  Mean   :15.4   Mean   : 42.98  
    ##  3rd Qu.:19.0   3rd Qu.: 56.00  
    ##  Max.   :25.0   Max.   :120.00

## Including Plots

You can also embed plots, for example:

![](images/pressure-1.png)<!-- -->

``` r
list.files("images",
           full.names = TRUE)
```

    ## [1] "images/pressure-1.png"

``` r
list.files("../cache")
```

    ## [1] "__packages"                                     
    ## [2] "cars_def0def16a33f1c2905394df0e332ca9.RData"    
    ## [3] "cars_def0def16a33f1c2905394df0e332ca9.rdb"      
    ## [4] "cars_def0def16a33f1c2905394df0e332ca9.rdx"      
    ## [5] "pressure_d7abd738a835d0facd36e90cc3ef3f98.RData"
    ## [6] "pressure_d7abd738a835d0facd36e90cc3ef3f98.rdb"  
    ## [7] "pressure_d7abd738a835d0facd36e90cc3ef3f98.rdx"

``` r
list.files("../images")
```

    ##  [1] "3953273590_704e3899d5_m.jpg"   "500x300.png"                  
    ##  [3] "bio-photo-2.jpg"               "bio-photo.jpg"                
    ##  [5] "browserconfig.xml"             "editing-talk.png"             
    ##  [7] "foo-bar-identity-th.jpg"       "foo-bar-identity.jpg"         
    ##  [9] "image-alignment-1200x4002.jpg" "image-alignment-150x150.jpg"  
    ## [11] "image-alignment-300x200.jpg"   "image-alignment-580x300.jpg"  
    ## [13] "manifest.json"                 "mstile-144x144.png"           
    ## [15] "mstile-150x150.png"            "mstile-310x150.png"           
    ## [17] "mstile-310x310.png"            "mstile-70x70.png"             
    ## [19] "paragraph-indent.png"          "paragraph-no-indent.png"      
    ## [21] "profile_picture_v2.jpeg"       "profile.png"                  
    ## [23] "safari-pinned-tab.svg"         "site-logo.png"

``` r
getwd()
```

    ## [1] "/Users/nicholascooley/Repos/Personal_Website/npcooley.github.io/_source"

``` r
file.copy(from = list.files("images",
                            full.names = TRUE),
          to = "../images/")
```

    ## [1] TRUE

``` r
file.remove(list.files("images",
                            full.names = TRUE))
```

    ## [1] TRUE

``` r
file.remove("images")
```

    ## [1] TRUE

Note that the `echo = FALSE` parameter was added to the code chunk to
prevent printing of the R code that generated the plot.
