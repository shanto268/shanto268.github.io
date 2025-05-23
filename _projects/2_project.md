---
layout: page
title: Muon Telescopes
description: Advanced Particle Detector Lab
img: assets/img/research/apd/thumbnail.png
importance: 2
category: undergrad-research
related_publications: true
giscus_comments: true
toc:
  sidebar: left
---

**Feb 2018 - July 2021**

This project was my entry point into the world of research—and it couldn't have been a better beginning. It was the first time physics stopped being just equations on a page and became something concrete, experimental, and real. I learned what it means to build hardware from the ground up, to collaborate in a lab where ideas move fast and hands do the work, and to chase questions that don't yet have answers. We were a small team building muon telescopes that could see through dense structures using nothing but cosmic rays.

Dr. Akchurin and Dr. Kunori were more than just exceptional scientists—they were patient, generous mentors who took the time to guide and challenge us. The lab became a foundation for how I think, work, and learn. A lot of what I do now traces back to that time. And one day, when I'm in a position to do so, I hope to support projects like this—because they open doors the way this one did for me.


## Project at-a-glance:

We developed portable, modular **muon telescopes** for high-resolution 3D imaging of dense structures via **muon tomography** {% cite 10.1063/10.0002046%}. By measuring how atmospheric muons scatter and lose energy while traversing materials, we could reconstruct internal densities—noninvasively, and with remarkable precision. These devices combined plastic scintillators, custom optical concentrators, SiPMs or PMTs, and complex software pipelines for event reconstruction.

## What I Did:

I wore many hats on this project—experimentalist, programmer, detector builder, problem solver—and somewhere in the middle of it all, both my love for experimental physics *and* my life as a programmer began. This was the first time physics stopped being abstract and became something hands-on, messy, and deeply rewarding. I joined the [**Advanced Particle Detector Lab**](https://www.depts.ttu.edu/phas/apdl/) during my sophomore year to get experience in real experimental physics—and I’ve been part of it ever since.

There’s no way I can explain everything I did here in any reasonable amount of time, but find below a rough sketch. Beyond any specific task, the most valuable thing I learned was how to **debug complex systems**—to think clearly when nothing is working, isolate failure modes, and engineer around chaos. That, and the eternal truth: **Vim >> Emacs**.

- **Optics and Signal Efficiency:** Started in the optics wing, where I helped design custom Winston cones to improve light collection. I fabricated over 50 scintillator bars, calibrated and installed 40 SiPMs and 44 PMTs, and increased our photon yield from ~20% to ~78%.

- **Telescope Hardware & Assembly:** Led the electrical and mechanical assembly of the full muon telescope system during the summer of 2019. Built and calibrated over 80 detection channels using SiPMs and PMTs, and learned practical fabrication and CAD skills in the process.

- **DAQ Systems (Arduino + CAMAC):** Developed the full data acquisition stack. Initially worked with Arduino-based DAQ and resolved severe bottlenecks by implementing a multithreaded sync mechanism. Later, transitioned to a **CAMAC-based system** and integrated FPGAs, reducing channel deadtime by ~300x. Codebases: [Arduino DAQ](https://github.com/shanto268/data_acquisition_code_arduino_ttumuon), [CAMAC Crates](https://github.com/shanto268/CrateCode), [DAQ Framework](https://github.com/shanto268/HEP_DAQ), and [Crate Analysis](https://github.com/shanto268/CrateAnalysis).

- **Geant4 Simulations:** Validated our detector design and experimental results through extensive Monte Carlo simulations. Contributed to modeling of scattering and absorption: [Prototype 1B](https://github.com/shanto268/mc_prototype_1b), [Prototype 2](https://github.com/shanto268/mc_prototype_2), [Two-Tray System](https://github.com/shanto268/mc_simulation_two_tray_system), and [WTP-focused MC](https://github.com/shanto268/monte_carlo_sim_muon_detector-wtp).

- **GUI-Driven Simulation Tools:** Built an interactive front-end for rapid geometry testing in Geant4: [muon simulation GUI](https://github.com/shanto268/mc_simulation_wtp_gui).

- **Signal Processing & Event Reconstruction:** Designed the analysis pipeline for converting raw signals to usable muon flux maps. Developed [event reconstruction and visualization tools](https://github.com/shanto268/event_display), along with [scattering analysis](https://github.com/shanto268/scattering_absorption_analysis) and [raw data analysis scripts](https://github.com/shanto268/muon_analysis_code_experimental_data_ttumuon).

- **Imaging & Contrast Enhancement:** Used contrast ratio methods for material discrimination: [ratio plot analysis](https://github.com/shanto268/ratio_plot_water_tower).

- **Machine Learning for Tomography:** Proposed and implemented the use of **Recurrent Neural Networks (RNNs)** and **LSTMs** to recover and interpolate missing hit data, improving the resolution of muon images by reducing data discards by 85%. Related repos: [focus stacking](https://github.com/shanto268/focus-stacking), [photon time studies](https://github.com/shanto268/PhotonTimeStudies), and [object detection analysis](https://github.com/shanto268/object_detection_analysis).


## Presentations:

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <iframe src="../../assets/img/research/apd/aps.pdf" width="100%" height="600px" class="rounded z-depth-1">
        </iframe>
    </div>
</div>

- APS March Meeting 2021 — Oral Presentation
- Texas Tech Physics Colloquium 2021
- APS Texas Section 2020 — Poster (UT Arlington)
- APS Texas Section 2019 — Poster (Texas Tech University)
- APS Far West Section 2019 (Stanford University) — Poster
- TTU Virtual Research Conference 2020 — Oral Presentation

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <iframe src="../../assets/img/research/apd/poster.pdf" width="100%" height="600px" class="rounded z-depth-1">
        </iframe>
    </div>
</div>

## Awards:

- TRUE Undergraduate Research Travel Award (2019)
- APS Travel Award (2019)
- First Place Poster, TTU Physics Department Poster Competition (2019)
- Outstanding Poster, APS Texas Section (2019) 
- Honorable Mention, APS Far West Section (2019)
