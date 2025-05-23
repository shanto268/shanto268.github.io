---
layout: page
title: Designing Superconducting Quantum Devices
description: Levenson-Falk Lab
img: assets/img/research/lfl/squadds.png
importance: 1
category: grad-research
related_publications: true
toc:
  sidebar: left
---


# `SQuADDS`

The SQuADDS (Superconducting Qubit And Device Design and Simulation) Database Project {% cite Shanto2024squaddsvalidated %} is an open-source resource aimed at advancing research in superconducting quantum device designs. It provides a robust workflow for generating and simulating superconducting quantum device designs, facilitating the accurate prediction of Hamiltonian parameters across a wide range of design geometries.

## Resources

**Paper Link:** [SQuADDS: A Database for Superconducting Quantum Device Design and Simulation](https://quantum-journal.org/papers/q-2024-09-09-1465/)

**GitHub Link:** [https://github.com/LFL-Lab/SQuADDS](https://github.com/LFL-Lab/SQuADDS)

**Docsite Link:** [https://lfl-lab.github.io/SQuADDS/](https://lfl-lab.github.io/SQuADDS/)

**Hugging Face Link:** [https://huggingface.co/datasets/SQuADDS/SQuADDS_DB](https://huggingface.co/datasets/SQuADDS/SQuADDS_DB)


## Project Presenations

### Quantum Device Workshop 2025

In this workshop, I introduced a machine learning–driven workflow for inverse design and interpolation of superconducting quantum devices using SQuADDS. We explored key challenges in mapping target Hamiltonians back to physical geometries, and demonstrated how tools like feature engineering, MLPs, LASSO, and KANs can extract structure from simulation data. Attendees worked through hands-on problems using real device data, connecting predictive modeling directly to EM simulation workflows in Palace.


### APS 2025 Global Physics Summit


At the [Quantum Device Workshop](https://qdw-ucla.squarespace.com/) hosted at UCLA, I was invited to lead both advanced and beginner sessions focused on SQuADDS and its applications in superconducting quantum device design. In the advanced track, I introduced a machine learning–driven workflow for inverse design and interpolation, demonstrating how to extract meaningful structure from simulation data and map desired Hamiltonian targets back to physical geometries using tools such as feature engineering, MLPs, LASSO, and KANs. Attendees worked hands-on with real device data and validated predictions through EM simulations in Palace.

<div class="d-flex justify-content-center my-3">
    <div class="col-sm mt-3" style="max-width: 700px;">
        {% include video.liquid path="https://www.youtube.com/embed/KPovj8B4gOU" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

For the beginner track, I guided participants through practical and efficient simulation workflows for superconducting quantum circuits. We explored how SQuADDS integrates with Qiskit-Metal to streamline the design process, from initial concept to fab-ready layout. The session emphasized building robust EM simulation pipelines and modeling devices with fabrication constraints in mind, providing a comprehensive introduction to realistic design iteration.


<div class="d-flex justify-content-center my-3">
    <div class="col-sm mt-3" style="max-width: 700px;">
        {% include video.liquid path="https://www.youtube.com/embed/XWx1su2HSIc" class="img-fluid rounded z-depth-1" %}
    </div>
</div>


### Qiskit Fall Fest 2024

The SQuADDS Tutorial lectures I have made for the workshop can be found [here](https://github.com/LFL-Lab/qiskit-fall-fest-2024-tutorials) for public access. I will link to the recordings once they are posted on YouTube.

#### SQUILL Foundry User Meeting 2024

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <iframe src="../../assets/img/research/lfl/shanto_LL_2024.pdf" width="100%" height="600px" class="rounded z-depth-1">
        </iframe>
    </div>
</div>

#### APS 2024 March Meeting

My talk at the [APS March Meeting 2024 - Session A47.8](https://meetings.aps.org/Meeting/MAR24/Session/A47.8) introduces the SQuADDS project and goes over an example workflow from Hamiltonian to GDS file.

<div class="d-flex justify-content-center my-3">
    <div class="col-sm mt-3" style="max-width: 700px;">
        {% include video.liquid path="https://www.youtube.com/embed/0bBYAHgYPzc" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
