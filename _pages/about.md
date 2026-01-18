---
permalink: /
title: "Biology, Software Development, and Bioinformatics at the edge of discovery"
output:
  md_document:
    variant: gfm
    preserve_yaml: TRUE
    toc: TRUE
    toc_depth: 3
knit: (function(inputFile, encoding) {
  rmarkdown::render(inputFile,
    encoding = encoding,
    output_dir = "../_pages") })
always_allow_html: true
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

- [About me](#about-me)
- [Current Role](#current-role)
- [Current Projects](#current-projects)
  - [BiocMetal](#biocmetal)
  - [SynExtend](#synextend)
  - [Others](#others)

# About me

I am a software engineer with a meandering work history, and highly
interdisciplinary training background. I received my undergraduate
degress in microbiology and molecular genetics from The Ohio State
University, and my Ph.D in organic chemistry from the University of
Missouri. I trained as a postdoc, first as a T15 training fellow, and
then as a regular postdoctoral researcher in the Department of
Biomedical Informatics at the University of Pittsburgh, and eventually
transitioned to a Research Software Engineer role at Pitt. I am
currently the Developer Engagement Lead for Bioconductor and am based
out of Limerick, Ireland.

# Current Role

My current role in developer engagement is funded through the Chan
Zuckerburg Institute, and has a broad mandate for improving developer
interactions with the Bioconductor project. This includes, but is not
limited; improving developer training resources, improving coding
practices and standards within the Bioconductor ecosystem, addressing
technical debt and planning for forward compatibility within the
Bioconductor ecosystem, and decreasing the technical and conceptual
gulfs between Bioconductor users who are not developers, and
bioconductor users who are very much developers.

My current role is a change of pace from solely software development and
an opportunity to have a bigger impact on how R as a language and
Bioconductor as a project can continue to play a pivotal role in
scientific discovery writ large, and both academic and non-academic
bioinformatics.

# Current Projects

In my current role, I have some flexibility to spend a small amount of
time on technical projects of my own. The following projects are under
current, albeit somewhat slow paced, development.

## BiocMetal

Robust and reliable programmatic access to GPU compute is still largely
absent from the R programming language. The reasons for this absence are
mostly historical, and I have started to explore ways to address that
gap in R and Bioconductor’s technical capabilities with a package
currently under the working name
[BiocMetal](https://github.com/npcooley/BiocMetal). Though this project
currently lends itself to more generalizable programmatic GPU compute,
ideally it will eventually encompass access to, and leveraging of, large
sequence based language models in R.

## SynExtend

[SynExtend](https://bioconductor.org/packages/release/bioc/html/SynExtend.html)
was originally envisioned as a relatively simple tool for performing
orthology inference from synteny maps alone. It has grown over time to
include contributions that are outside of that scope and is still a work
in progress. Development, validation, and testing of tools within the
package is ongoing.

## Others

I am generally excited to lend my expertise to projects that can benefit
from my unconventional mix of skills and experience. Feel free to reach
out!
