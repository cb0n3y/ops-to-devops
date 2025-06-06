# Prometheus Lab

This folder contains the lab setup and resources related to Prometheus monitoring.

## Overview

The purpose of this lab is to experiment with Prometheus configurations, scraping targets, and alerting rules in a controlled environment.

## Folder Structure

- **config/**  
  Contains the main Prometheus configuration files such as `prometheus.yml`.

- **rules/**  
  Contains Prometheus alerting and recording rule files.

- **targets/**  
  Contains target configuration files to define which endpoints Prometheus should scrape.

## Usage

- Use the configuration files in `config/` to deploy Prometheus in your lab environment.
- Add or modify alerting rules in the `rules/` directory.
- Manage your scrape targets in the `targets/` directory.
- Automate deployment or configuration updates using any helper scripts you place in the lab or shared-scripts folders.

## Notes

- This lab setup is for learning and testing purposes and is not intended for production.
- Keep all configurations under version control for traceability and easy rollback.
