---
marp: true
title: Product Documentation Presentation
paginate: true
theme: custom-theme
backgroundColor: #f8f8f8
---

<!--
CUSTOM THEME SECTION
You may place this at bottom too.
-->

<style>
/* === Custom Theme === */
section {
  background-size: cover;
  font-family: "Roboto", sans-serif;
}

h1, h2 {
  color: #004c99;
}

footer {
  font-size: 12px;
  color: #555;
}

:root {
  --slide-width: 1024px;
}

/* Page numbers on footer */
section::after {
  content: counter(page);
  position: absolute;
  bottom: 12px;
  right: 20px;
  color: #333;
}
</style>

---

# Product Documentation

**Author:** 23f3000686@ds.study.iitm.ac.in  
**Role:** Technical Writer

- Version controlled with Git
- Convertible to HTML, PDF, PPT

---

# Key Features

- Lightweight format (Markdown)
- Repeatable builds
- CI/CD friendly
- Export with:
