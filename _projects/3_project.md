---
layout: page
title: Microsimulation Traffic Calibration
description: Institute For Software Integrated Systems
img: assets/img/research/work-lab/thumbnail.png
importance: 3
category: undergrad-research
giscus_comments: true
toc:
  sidebar: left
related_publications: true
---

**Summer 2020**

## Project at-a-glance:

Traffic is known to exhibit complicated, nonlinear behavior that often results in so-called **phantom traffic jams** in which traffic jams can appear seemingly from thin air. These jams are known to cause decreases in fuel efficiency, increases in commute time, and decreases in driver safety. Watch this excellent Ted Ed video by one of my advisors in this project, [Benjamin Seibold](https://math.temple.edu/~seibold/) to learn more about phantom traffic jams:

<div class="row mt-3">
    <div class="col-sm mt-3">
        {% include video.liquid path="https://www.youtube.com/embed/TNokBgtSUvQ" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

An emerging technology for attempting to mitigate this phenomenon is the use of Connected and Autonomous Vehicles (CAVS) and machine learning, which employ novel control methods specifically designed for stopping phantom jams. This is one of the main focuses of the [CIRCLES project](https://circles-consortium.github.io/) which seeks to extend this technology to real-world traffic. 

## My Involvement: 

Under the guidance of [George Gunter and Daniel Work](https://lab-work.github.io/), I have worked on tackling the problem: **What can we infer about individual driver behavior from aggregate traffic data?** This is a crucial question for the development of the CAVS technology as it allows for the accurate modeling of traffic flow and the development of control algorithms. Read our paper {% cite Shanto2021microsimulationtraffic %} to learn more about our work in details and/or follow along below for a brief overview.

### Challenges in Calibrating Driver Models with Aggregate Traffic Data

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/research/work-lab/Network_Graphic.png" title="network.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
  A graphic representing the road geometry combined with a single radar sensor generating aggregate speed measurements.
</div>

One of the core challenges in using aggregate data (e.g., average speed from sensors) to study individual driver behavior lies in calibrating traffic models under conditions that may lead to instability. Traditional traffic models like the **Intelligent Driver Model (IDM)** can simulate individual vehicle behaviors, capturing nonlinear interactions that give rise to traffic waves—oscillations in speed and spacing that can even create **phantom traffic jams**. However, calibrating IDM to reflect real-world traffic behavior accurately is complex because not all model parameters impact observable average-speed data directly.


#### Introducing the Intelligent Driver Model (IDM)

The **Intelligent Driver Model (IDM)** is a widely-used car-following model in traffic simulations designed to describe the acceleration and braking behavior of individual vehicles based on surrounding traffic conditions. IDM defines a vehicle’s acceleration at any point in time as a function of its current speed, the gap to the vehicle in front, and the relative speed between the two vehicles. This model is particularly effective for capturing both smooth traffic flows and the sudden transitions to stop-and-go waves that often characterize congested traffic.

The IDM acceleration equation is:

\begin{equation}
\frac{d v}{d t} = a \left( 1 - \left( \frac{v}{v_0} \right)^{\delta} - \left( \frac{s^*(v, \Delta v)}{s} \right)^2 \right)
\end{equation}

where:
- $$v$$ is the current velocity of the vehicle,
- $$v_0$$ is the desired speed (or "free flow" speed),
- $$a$$ is the maximum acceleration,
- $$\delta$$ is the acceleration exponent, typically set to 4 for IDM,
- $$s$$ is the gap to the leading vehicle,
- $$s^*(v, \Delta v)$$ is the desired safe distance, calculated as:

\begin{equation}
s^*(v, \Delta v) = s_0 + v T + \frac{v \Delta v}{2 \sqrt{a b}}
\end{equation}

In this expression:
- $$s_0$$ represents the minimum gap (or stopping distance) at zero speed,
- $$T$$ is the desired time gap between vehicles,
- $$\Delta v$$ is the relative speed with the car ahead,
- $$b$$ is the comfortable braking deceleration.

The IDM is effective in simulating realistic driver behaviors in various traffic situations. Under stable conditions, it maintains smooth flow, while under disturbed conditions, it naturally gives rise to stop-and-go waves. This behavior makes IDM well-suited for studying traffic instabilities and understanding the formation of **phantom traffic jams**.

In this project, we aim to calibrate parameters controlling traffic stability—parameters which typically do not influence **equilibrium traffic states** but are critical in determining whether a steady flow will hold or break into stop-and-go waves. For instance, IDM’s stability parameters, $$a$$ and $$b$$, play a significant role in whether traffic flow remains smooth or develops waves in response to perturbations.

#### The Calibration Process

To address this, we set up a simulation framework where IDM’s parameters can be calibrated against sensor data in a single-lane traffic model. Using aggregate measurements, we solve an optimization problem that minimizes the difference between simulated and real traffic data. The calibration setup is structured as follows:

- **Objective Function**: The goal is to find the parameter set $$\theta = (a, b)$$ that best fits the observed data by minimizing a loss function:

  \begin{equation}
  \underset{\theta}{\text{minimize}} \, L(Y_{\text{obs}}, Y_{\text{sim}}(\theta))
  \end{equation}

  where:
  - $$Y_{\text{obs}}$$ represents real-world measurements (e.g., from roadside sensors),
  - $$Y_{\text{sim}}(\theta)$$ denotes the simulated output under a given parameter choice,
  - $$L$$ is a loss function, such as Root Mean Square Error (RMSE), which quantifies the difference between the real and simulated data.

- **Optimization Techniques**: Various optimizers, including Nelder-Mead and Least Squares, were tested. However, results showed that standard loss functions like RMSE often misidentify parameter values in unstable traffic states, highlighting the need for refined calibration methods.

- **Parameter Sweeping**: To accurately capture parameter sensitivity, we employed a brute-force approach, systematically sweeping across values of $$a$$ and $$b$$ to understand their influence on traffic wave dynamics.


### Insights and Implications for Traffic Modeling

Our findings indicate that standard calibration methods may return inaccurate parameter estimates, especially in scenarios where traffic is unstable. Traffic waves emerge differently based on small variations in the parameters, which in turn alter the loss landscape, making calibration challenging. This variability suggests that additional or alternative loss functions might be needed to capture the effects of stability parameters accurately.

## Project Presenations

#### SummerShowcase 2021

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <iframe src="https://cps-vo.org/sites/cps-vo.org/files/cpsvo_file_nodes/Summer_Showcase.pdf" width="100%" height="600px" class="rounded z-depth-1">
        </iframe>
    </div>
</div>


#### Poster Presentation

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <iframe src="../../assets/img/research/work-lab/vu_calibration.pdf" width="100%" height="600px" class="rounded z-depth-1">
        </iframe>
    </div>
</div>