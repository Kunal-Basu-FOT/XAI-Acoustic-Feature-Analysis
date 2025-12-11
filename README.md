# XAI-Acoustic-Feature-Analysis

This repository contains my research on applying **Explainable AI (XAI)** to identify the acoustic features that drive **voice-recognition models**. The project combines classical signal processing with model-agnostic interpretability methods to understand how different classifiers use spectral information to distinguish speakers, including challenging cases such as **identical twins**.

This work was **accepted for presentation** at the  
**International Conference on Innovations in Science and Technology: A Perspective of Viksit Bharat@2047 (2025)**  
Track 5: *Frontiers in Physics and Emerging Trends in Electronics*.

## 🔍 Overview

The study evaluates four machine-learning models:

- **k-Nearest Neighbors (KNN)**
- **Support Vector Machine (SVM, RBF kernel)**
- **Random Forest (RF)**
- **Multilayer Perceptron (MLP)**

All models were trained on a dataset of student voice samples collected at the Faculty of Technology, University of Delhi.  
Preprocessing included **normalisation**, **framing**, and extraction of:

- **MFCCs (1–13)**
- **Short-Time Energy (STE)**
- **Zero-Crossing Rate (ZCR)**
- **Pitch and fundamental frequency features**
- **DCT-based spectral coefficients**

Model evaluation used a **70:30 train-test split**, confusion matrices, and accuracy metrics.

## 🎯 Key Results

- All models achieved **>95% classification accuracy**.  
- XAI analysis using **LIME** revealed architecture-specific reliance on MFCCs:
  - **Random Forest:** MFCC 13 (high-frequency variation).
  - **MLP:** MFCC 2 and MFCC 8 (broad spectral shape + fine structure).
  - **SVM (RBF):** MFCC 3 and MFCC 8.
  - **KNN:** MFCCs 4, 9, and 11.
- Identical-twin experiments show that subtle spectral cues are sufficient for consistent classification when interpreted through MFCC-based structure.
- Study demonstrates that high accuracy alone does not reveal *why* decisions are made—XAI provides the missing interpretive layer.

## 🧠 Purpose

This project highlights how **classical spectral features interact with classifier geometry**, and how **XAI can expose the decision boundaries** driving acoustic recognition. The goal is to make voice-based systems more transparent, robust, and interpretable—especially in biometric and security contexts.

## 📘 Citation

Basu, Kunal (2024). *Explainable Acoustic Feature Interpretation in Voice Recognition Models*.  
Presented at **Innovations in Science and Technology: A Perspective of Viksit Bharat@2047**,  
Deen Dayal Upadhyaya University, New Delhi.


