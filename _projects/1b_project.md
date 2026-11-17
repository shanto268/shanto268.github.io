---
layout: page
title: Foundational ML Model for Physics
description: Levenson-Falk Lab
seo_title: QCap — capacitance matrix of any planar superconducting layout
seo_description: QCap is Sadman Ahmed Shanto's physics-corrected graph neural network that predicts the full Maxwell capacitance matrix of any planar superconducting circuit layout from its GDS file, released open source in SQuADDS.
keywords: QCap, SQuADDS, capacitance matrix, graph neural network, physics-informed machine learning, superconducting qubits, GDS, Ansys Q3D, method of moments, AI for science
img: assets/img/research/lfl/qcap.png
importance: 1
category: grad-research
toc:
  sidebar: left
---

# QCap

QCap predicts the full Maxwell capacitance matrix of any planar superconducting circuit layout straight from its GDS file, in about a second on a laptop instead of minutes to hours of Ansys Q3D simulation. It reads every metal piece of the layout as a node of a graph, so it works for any layout made with any tool, and it never merges nets: an N-conductor layout gets its full N x N matrix.

The model is physics first. A fast thin-film method-of-moments solve gives a first estimate of how every pair of conductors couples, and a graph neural network, trained on about 40,000 Ansys Q3D simulations, learns the correction. On a family of layouts that no part of the model saw in training, QCap's median error is 1.05 % (MAE 0.132 fF, RMSE 0.188 fF).

QCap is open source in [SQuADDS](https://github.com/LFL-Lab/SQuADDS) (`pip install "squadds[ml]"`), with the dataset, the models, a browser demo and a hosted API. The preprint is coming very soon.

<div class="d-flex justify-content-center my-3">
    <div class="col-sm mt-3" style="max-width: 700px;">
        {% include video.liquid path="https://lfl-lab.github.io/SQuADDS/qcap/media/v1_summary.mp4" class="img-fluid rounded z-depth-1" controls=true poster="https://lfl-lab.github.io/SQuADDS/qcap/media/v1_summary.jpg" %}
    </div>
</div>

## Resources

**Paper Docsite:** [https://lfl-lab.github.io/SQuADDS/qcap/](https://lfl-lab.github.io/SQuADDS/qcap/), the paper section by section with short videos

**Browser Demo:** [https://huggingface.co/spaces/SQuADDS/planar-capacitance](https://huggingface.co/spaces/SQuADDS/planar-capacitance)

**Models:** [https://huggingface.co/SQuADDS/QCap](https://huggingface.co/SQuADDS/QCap)

**Dataset:** [https://huggingface.co/datasets/SQuADDS/SQuADDS_PlanarCapacitance](https://huggingface.co/datasets/SQuADDS/SQuADDS_PlanarCapacitance)

**Docs and Tutorials:** [ML Models guide](https://lfl-lab.github.io/SQuADDS/source/ml_models.html#planar-capacitance-models) and Tutorials 11-16

**Code:** [https://github.com/LFL-Lab/SQuADDS](https://github.com/LFL-Lab/SQuADDS)
