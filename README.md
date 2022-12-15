<div id="top"></div>

[![LinkedIn][linkedin-shield]][linkedin-url]
![Generic badge](https://img.shields.io/badge/Project-Pass-green.svg)

<!-- PROJECT HEADER -->
<br />
<div align="center">
  <a href="#">
    <img src="images/udacity.svg" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">TechTrends Cloud Native Application Architecture</h3>

  <p align="center">
    Cloud native solution for online news sharing platform 
    <br />
    <br />
    -----------------------------------------------
    <br />
    <br />
    Data Engineer for AI Applications Nanodegree
    <br />
    Bosch AI Talent Accelerator Scholarship Program
  </p>
</div>

<br />

<!-- TABLE OF CONTENTS -->
<details open>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#application-deployment-locally">Application Deployment Locally</a></li>
    <li><a href="#application-packaging-using-docker">Application Packaging Using Docker</a></li>
    <li><a href="#continuous-integration-with-github-actions">Continuous Integration with GitHub Actions</a></li>
    <li><a href="#kubernetes-cluster-using-declarative-manifests">Kubernetes Cluster Using Declarative Manifests</a></li>
    <li><a href="#continuous-delivery-with-argocd">Continuous Delivery with ArgoCD</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<br/>

<!-- ABOUT THE PROJECT -->

## About The Project

TechTrends is an online website used as a news sharing platform, that enables consumers to access the latest news within the cloud-native ecosystem. In addition to accessing the available articles, readers are able to create new media articles and share them.

The project includes a complete solution to package and deploy the application to a Kubernetes platform. The project utilized Docker to package the application and automated the Continuous Integration process with GitHub Actions. For the release process, Kubernetes' declarative manifests have been used, which were templated using Helm. To automate the Continuous Delivery process, we have used ArgoCD.

The web application itself is written using the Python Flask framework. It uses SQLite, a lightweight disk-based database, to store the submitted articles.

Below, you can examine the main components of the first prototype of the application:

![App Components][app-components]

<br />

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

-   [![Python][python-shield]][python-url]
-   [![DOCKER][docker-shield]][docker-url]
-   [![VAGRANT][vagrant-shield]][vagrant-url]
-   [![KUBERNETES][kubernetes-shield]][kubernetes-url]
-   [![GITHUB-ACTIONS][github-actions-shield]][github-actions-url]
-   [![VSCode][vscode-shield]][vscode-url]

<p align="right">(<a href="#top">back to top</a>)</p>

## Application Deployment Locally

![Application Deployment Locally][local-app]

<p align="right">(<a href="#top">back to top</a>)</p>

## Application Packaging Using Docker

![Application Packaging Using Docker][package-app]

<p align="right">(<a href="#top">back to top</a>)</p>

## Continuous Integration with GitHub Actions

![Continuous Integration with GitHub Actions][ci-github-actions]

<p align="right">(<a href="#top">back to top</a>)</p>

## Kubernetes Cluster Using Declarative Manifests

![Kubernetes Cluster Using Declarative Manifests][kubernetes-cluster]

<p align="right">(<a href="#top">back to top</a>)</p>

## Continuous Delivery with ArgoCD

![Continuous Delivery with ArgoCD Staging][argocd-staging]

</br>

![Continuous Delivery with ArgoCD Prod][argocd-prod]

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

-   [Udacity](https://www.udacity.com/)
-   [Bosch AI Talent Accelerator](https://www.udacity.com/scholarships/bosch-ai-talent-accelerator)
-   [Img Shields](https://shields.io)
-   [Best README Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- SHIELDS -->

[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[docker-shield]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[github-actions-shield]: https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white
[kubernetes-shield]: https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white
[vagrant-shield]: https://img.shields.io/badge/vagrant-%231563FF.svg?style=for-the-badge&logo=vagrant&logoColor=white
[vscode-shield]: https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white

<!-- LINKS -->

[linkedin-url]: https://www.linkedin.com/in/arfat-mateen
[python-url]: https://www.python.org/
[docker-url]: https://www.docker.com/
[github-actions-url]: https://github.com/features/actions
[kubernetes-url]: https://kubernetes.io/
[vagrant-url]: https://www.vagrantup.com/
[vscode-url]: https://code.visualstudio.com/

<!-- IMAGES -->

[app-components]: images/app_components.png
[local-app]: screenshots/docker-run-local.png
[package-app]: screenshots/ci-dockerhub.png
[ci-github-actions]: screenshots/ci-github-actions.png
[kubernetes-cluster]: screenshots/kubernetes-declarative-manifests.png
[argocd-staging]: screenshots/argocd-techtrends-staging.png
[argocd-prod]: screenshots/argocd-techtrends-prod.png
