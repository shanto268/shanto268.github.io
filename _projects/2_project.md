---
layout: page
title: Muon Telescopes
description: Advanced Particle Detector Lab
img: assets/img/research/apd/thumbnail.png
importance: 2
category: undergrad-research
giscus_comments: true
toc:
  sidebar: left
---

This was my first real dive into science and research—an unforgettable experience that shaped how I approach problems, collaboration, and technology. I got to be part of something much bigger than myself, surrounded by brilliant people, building actual instruments that detect particles from space. It doesn’t get cooler than that.

I’m deeply grateful to the lab, the professors (Dr. Akchurin and Dr. Kunori - UNBELIEVABLY AMAZING INDIVIDUALS), and my wonderful colleagues—none of this would’ve been possible without their mentorship, patience, and support. One day, when I *do* have the moneys™, I promise I’ll help fund projects like this.

## Project at-a-glance:

We built compact, modular **muon telescopes** capable of detecting cosmic ray muons to perform 3D imaging of dense objects—a technique known as **muon tomography**. These telescopes use plastic scintillators, light guides (like Winston cones), and silicon photomultipliers (SiPMs) to detect particle tracks, and software pipelines to reconstruct internal structures of scanned volumes.

## My Involvement: 

We got a paper out for **Prototype v1** [{% cite 10.1063/10.0002046 %}]—not exactly Pulitzer material, but hey, it's peer-reviewed and it's real. That said, the majority of what I worked on didn't make it into a formal publication (classic research life), so this docsite is a tribute to all that off-paper but not-off-value work.

### Winston-Cones:

I contributed to the design and manufacturing process of Winston cones—non-imaging light concentrators that guide photons from scintillators into SiPMs with minimal loss. We prototyped multiple geometries and reflective coatings to optimize light collection efficiency.

### Monte-Carlo Simulations:

I ran Geant4-based Monte Carlo simulations to understand particle trajectories, energy deposition profiles, and optimize detector geometry for different target materials. These simulations informed design tweaks and shielding strategies.

### Readout Electronics Setup:

Helped build and debug the entire readout chain: custom amplifier boards, biasing circuits for SiPMs, digitizers, and a triggering logic system. Got a crash course in signal integrity, grounding nightmares, and just how noisy the real world is.

### Prototype v1 Assembly and Data Taking:

I was on the team that physically assembled and deployed the first working version of the telescope. We ran calibration routines using cosmic muons and radioactive sources, and collected the data used in our first publication.

### Prototype v2 Assembly:

Led much of the mechanical integration work for Prototype v2. This version was sleeker, more modular, and easier to align. Learned the joys of 3D CAD, acrylic machining, and adhesive regrets.

### Prototype v2 DAQ Setup:

Wrote Python scripts for automated data acquisition, timestamp synchronization, and hit reconstruction. Also implemented remote monitoring tools to keep tabs on the system during long runs.

### Muon Tomography Software:

Contributed to developing the 3D reconstruction pipeline: from raw hit processing to event filtering and voxel-wise tomographic inversion. Integrated statistical priors for noise suppression and improved spatial resolution.

### Muon2Photon Analysis with RNNs:

Started an exploratory project using recurrent neural networks to classify muon events and distinguish them from potential gamma/electron backgrounds. Early results were promising, but this was cut short before full deployment.

### 3D Tomograph Generation:

Helped render 3D tomographic images of scanned objects. Used voxel-based mapping techniques and visualized reconstructed densities using custom OpenGL and matplotlib pipelines. Looked pretty. Felt cooler.

## Presentations:

- Poster and oral presentation at [insert conference name]
- Internal lab seminars and demo day showcases
- Outreach talk for high school students interested in physics

## Achievements and Awards:

- Undergraduate Research Grant Recipient
- Best Poster Award at [insert applicable event]
- Invited speaker at [insert if any]

