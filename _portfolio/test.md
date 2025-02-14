---
title: "Using SynExtend - Simple"
excerpt: "A simple workflow with SynExtend, simply using a synteny map to perform orthology inference between two genomes."
collection: portfolio
output:
  md_document:
    variant: gfm
    preserve_yaml: TRUE
    toc: TRUE
    toc_depth: 3
knit: (function(inputFile, encoding) {
  rmarkdown::render(inputFile,
    encoding = encoding,
    output_dir = "../_portfolio") })
always_allow_html: true
---

- [header 1](#header-1)
  - [subheader 1](#subheader-1)
  - [R Markdown](#r-markdown)
- [header 2](#header-2)
  - [Including Plots](#including-plots)
    - [minor header](#minor-header)
- [header 3](#header-3)

# header 1

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
    ## [21] "pressure-1.png"                "profile_picture_v2.jpeg"      
    ## [23] "profile.png"                   "safari-pinned-tab.svg"        
    ## [25] "site-logo.png"                 "stack-1.png"

## subheader 1

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

# header 2

## Including Plots

### minor header

You can also embed plots, for example:

![](/images/pressure-1.png)<!-- -->

![](/images/stack-1.png)<!-- -->

# header 3

Note that the `echo = FALSE` parameter was added to the code chunk to
prevent printing of the R code that generated the plot.
