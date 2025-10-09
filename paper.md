---
numbering:
  heading_2: false
  figure:
    template: Fig. %s
---

## Can sex-specific neurotransmitter dynamics allow tailored treatment? 

## *A preview from a dashboard.*

### Introduction

Stroke remains a major global public health issue, profoundly affecting individuals' quality of life through a wide range of consequences, including aphasia, motor and sensory deficits, behavioral changes, and even death (Brain Injury Canada, 2024). It is among the most devastating non-communicable diseases (NCDs), ranking second in global mortality and third in combined mortality and disability. Globally, by age 25 one in four adults is expected to experience a stroke in their lifetime, and more than half of these events will occur before the age of 70. In 2021, nearly 12 million people experienced a first-ever stroke, of which 65.3% were ischaemic, and 52.6% occurred in men (Feigin et al, 2025). Despite the slightly higher incidence in men, women who survive a stroke often experience more severe long-term disability. This difference is partly attributed to the older average age at which women suffer strokes and to the loss of estrogen's neurovascular protection after menopause. Knowing that estrogen and progesterone enhance vasodilatation effects, whereas testosterone is believed to have opposed vascular effects (Haast et al., 2012).

Ischaemic stroke results from an obstruction of cerebral blood flow, usually due to a thrombus or embolus, while haemorrhagic stroke is caused by bleeding from a ruptured vessel. Although less frequent, haemorrhagic strokes typically result in more severe brain damage and have a higher fatality rate (Andersen et al., 2009). The present study focuses exclusively on ischaemic stroke, particularly those resulting in aphasia since it affects approximately 1/3 of stroke patients (Pedersen et al., 1995). While stroke recovery has been widely studied, sex-specific mechanisms underlying aphasia recovery remain underexplored, especially in the acute phase (<72 hours post-stroke). 
Recent advances in molecular neuroimaging offer novel tools to explore these mechanisms. Hansen et al. recently published a neurotransmitter atlas of normative receptor and transporter densities maps, which was later used by Alves et al. to develop an MRI white matter atlas of neurotransmitter circuits representing the axonal projections of acetylcholine, dopamine, noradrenaline, and serotonin receptors and transporters. Their method allows to chart how stroke damages neurotransmitter systems, which distinguishes pre and postsynaptic disruption. Their method offers a promising approach to customize stroke treatment based on individual profiles.

Nevertheless, there is still limited understanding of how biological sex modulates early neurotransmitter dynamics following stroke. In particular, the role of key neurotransmitters involved in language and memory, such as the ones used by Alves et al. to develop their tool and also glutamate, and γ-aminobutyric acid (GABA), remains underexplored in the context of sex-specific recovery trajectories after stroke. These neurotransmitters are all relevant to cognitive and linguistic functions. Identifying sex-linked neurochemical differences in these systems could pave the way for more personalized therapeutic strategies

The objective of this study is twofold: (1) to determine whether and how biological sex influences neurotransmitter receptor and transporter dynamics during the acute phase of post-stroke aphasia; and (2) to assess whether these early neurochemical patterns can help predict long-term language recovery. Ultimately, this work aims to contribute to more personalized stroke rehabilitation approaches, including the tailored use of receptor agonists or transporter inhibitors, recognizing that men and women may respond differently to the same pharmacological intervention.

### Materials and methods

#### Participants

Forty-eight individuals with aphasia (PWA) were recruited from the Neurology Unit of the Hôpital du Sacré-Cœur de Montréal (HSCM), part of the CIUSSS du Nord-de-l’Île-de-Montréal. Sixteen participants were later excluded due to the following reasons: brain tumors, right or bilateral stroke, left-handedness, MRI intolerance, multiple strokes, or voluntary withdrawal/refusal to continue participation. Ultimately, fifteen participants completed all three timepoints up to the chronic phase.
Inclusion criteria for PWA were: (1) first-ever left-hemispheric ischemic stroke in the middle cerebral artery (MCA) territory; (2) presence of aphasia affecting speech production and/or comprehension in the acute phase; (3) native French speaker; (4) aged 18 to 85; and (5) right-handed. Exclusion criteria included: (1) major psychiatric illness; (2-3) history of traumatic brain injury or intracranial surgery; (4) alcoholism or drug abuse; (5) learning disability; (6) uncorrected hearing or vision problems; (7) MRI contraindications (e.g., metallic implants or claustrophobia); (8) aphasia due to a subthalamic stroke; (9) pronounced subcortical arteriosclerosis. No exclusion was made based on aphasia severity or lesion size in the acute phase. Participants enrolled in active speech-language therapy at the time of recruitment were also excluded.
MRI acquisition and lesion processing

Participants underwent MRI scans at three timepoints: (1) ≤3 days post-stroke (acute phase), (2) 10–14 days (subacute phase), and (3) 6–12 months (chronic phase). Longitudinal T1-weighted images were processed using FreeSurfer to create within-subject templates. Diffusion-weighted and T1-weighted images were processed using the TractoFlow pipeline (Theaud et al., 2020), generating diffusion tensor metrics: fractional anisotropy (FA), axial diffusivity (AD), and radial diffusivity (RD).
Lesion segmentation was performed semi-automatically using the Clusterize toolbox on MD maps in the acute and subacute phases, and on RD(AD?) maps for the chronic phase. All lesion segmentations were manually reviewed and corrected by an experienced researcher in tracing lesions in PWA. Binary lesion masks were then created at each timepoint in RAS orientation (1 mm isotropic resolution). These masks and corresponding anatomical images were transformed into MNI152 2 mm space using FSL’s FLIRT (nearest-neighbor interpolation, no smoothing, zero padding). The NeuroTmap pipeline (Alves et al., 2025) was applied to compute neurotransmitter-specific lesion’s metrics, including sum of receptor and transporter’s location density map voxels or white matter projection map voxels intersected by the lesion, and pre- and postsynaptic ratios of the studied neurotransmitters systems. The NeuroT-Map tool and associated scripts are publicly available on GitHub at: https://github.com/Pedro-N-Alves/NeuroT-Map?tab=readme-ov-file. 

#### Language Assessment

At each timepoint, participants underwent a comprehensive language evaluation designed specifically for PWA by Dr. Brambati and collaborators (Drs. Rochon, Leonard and Marcotte). The battery included:

- Naming: DO-80, (Deloche et al., 1997) Boston naming test (Kaplan et al., 1983)
- Verbal fluency:  Montréal Évaluation de la Communication (MEC) (Joanette et al., 2004). 
- Word and pseudoword repetition: Montréal-Toulouse-86 (MT-86) (Nespoulous et al., 1992)
- Sentence comprehension: MT-86 (Nespoulous et al., 1992), Token test (Renzi et al., 1978)
- Spontaneous speech: Western Aphasia Battery (Kertesz, 2006)
- Dysarthria: Robertson dysarthria profile (Robertson, 1987)
- Semantics: Pyramid and Palm Tree Test (Howard et al., 1992)
- Executive Function: Ruff Figural Fluency Test (Ruff, 1986)
- Visual Neglect: Bells Test (Gauthier et al., 1989)

These tests have been found to be acceptable, reliable, and valid measures for PWA (Wallace et al., 2017). All assessments were conducted by a certified speech-language pathologist. Audio-video recordings were used to ensure reliability. Three core language subscores were derived: naming, repetition, and comprehension. Based on the previous work of Osa García et al., each subscore was scaled from 0 to 10 based on task-specific maximums, yielding a total aphasia severity index, named the Composite Score, ranging from 0 to 30.

#### Statistical Analysis 

We performed a series of generalized linear models (GLMs) using a Tweedie distribution (variance power =1.4) with a logarithmic link function to accommodate continuous outcomes with skewed distributions and potential zero-values. In the acute full-sample analysis (n = 32), models included interaction terms between sex, lesion volume, and age to explore their potential modulatory effects on the relationship between acute phase neurotransmitter metrics (voxelwise damage to density and projection maps, as well as pre- and post-synaptic ratios) and early language outcomes. We also ran stratified GLMs in men and women separately, without interaction terms but controlling for lesion volume. Finally, an additional GLM was conducted using acute-phase neurotransmitter metrics as early predictors of chronic-phase language outcomes (n=16), adjusting for sex and lesion volume as covariates.

Additionally, two-sample tests (Student’s or Welch’s t-test, or Mann–Whitney U test) were used depending on the normality (Shapiro–Wilk test) and variance homogeneity (Levene’s test). Comparisons were performed between men and women separately for each predictor and outcome variable in the acute phase (nm=19; nf=13), as well as for group-level differences across timepoints (e.g., acute vs. chronic assessments; nm=7; nf=9). The significance threshold was set at α = 0.05 (with the Benjamini-Hochberg false discovery rate correction).

Linear mixed models (LMMs) with time (acute, subacute, chronic) and biological sex as fixed effects were conducted to evaluate longitudinal changes in language scores. Pearson or Spearman correlations were computed between neurotransmitter ratios, between ratios and clinical scores, and between damage metrics and outcomes. All correlation tests were performed separately and jointly for males and females in the acute phase. Also, same correlation tests were made with acute metrics and chronic outcomes. Group-level descriptive statistics (mean, median, SD) were also computed.

### Results

We first examined sex-related differences in neurotransmitter system disruption and language outcomes during the acute phase after stroke, and whether early post-stroke imbalance could predict long-term language recovery.

To visualize disruptions, group-averaged male (n = 23) and female (n = 15) data were overlaid on circular graphs showing lesion effects on receptor/transporter density maps, tract projection maps, and derived synaptic disruption ratios (Fig.1), computed with the NeuroT-Map method by Alves et al.. Note that these sample sizes differ from those used for statistical analyses, as not all participants had clinical data but all had lesion masks.

:::{figure} #fig1cell
:label: fig1
:name: fig1

Ma figure interactive avec contrôles Plotly
:::


<!-- [Voir Figure 1 interactive] https://mybinder.org/v2/gh/moranebienvenu/stroke_article/tree/main/HEAD?urlpath=%2Fdoc%2Ftree%2Fcontent%2Ffigure_1.ipynb -->

<!-- [](https://doi.org/10.31219/osf.io/h89js) -->
<!-- :::{figure} static/banner.jpg -->

<!-- A funny take on the difference between articles with code and articles from code.
:::

Let's see how directives work with a simple example by rendering a video from an external source:

:::{iframe} https://cdn.curvenote.com/0191bd75-1494-72f5-b48a-a0aaad296e4c/public/links-8237f1bb937ea247c2875ad14e560512.mp4
:label: figvid
:width: 100%

Video reused from [mystmd.org](https://mystmd.org) (CC-BY-4.0, [source](https://mystmd.org/guide)).
:::

Yet, the main purpose of this article is to not to showcase all the [authoring tools](https://mystmd.org/guide/typography) available in MyST Markdown, but rather to provide a simple template to get you started with your own article to publish on NeuroLibre.


:::{seealso}
You can refer to the [MyST Guide](https://mystmd.org/guide/typography) to see all the cool stuff you can do with MyST Markdown, such as creating a `mermaid` diagram like this:


Or you can see how hover-over links work for [wikipedia sources](https://en.wikipedia.org/wiki/Wikipedia#:~:text=Wikipedia%20is%20a%20free%20content,and%20the%20wiki%20software%20MediaWiki.) and cross references figures (e.g., [Fig. %sf](#fig1), [Figure %sf](#fig2), [Video %sf](#figvid)).
:::

Typically, when publishing an article following the traditional route, you would write your article in a word processor where you need to deal with the generation of figures, tables etc. elsewhere, and then bring them together in the final document manually. This eventually leads to a cluttered set of files, code, dependencies, and even data that are hard to manage in the long run. If you've been publishing articles for a while, you probably know what we are talking about:

> Where is the endnote reference folder I used for this article? -->

<!-- > What is the name of the script I used to generate the second figure? This script has the title `fig_2_working.py` and is in the  `karakuzu_et_al_2016_mrm` folder, but it does not seem to be the one that generated the figure... --> -->

<!-- > I cannot create the same runtime environment that I used for this analysis in my current project because `python 3.8` is not available in the current distribution of Anaconda... It is so tricky to get this running on my new computer...

MyST Markdown offers a powerful solution to this by allowing you to create an article ✨from code✨, linking all the pieces of your executable and narrative content together in the body of this one document: your canvas.

:::{figure} https://cdn.curvenote.com/0191bd75-1494-72f5-b48a-a0aaad296e4c/public/reuse-jupyter-output-2e6bfa91772dbb6bbc022dc6aee80d2b.webp
:label: fig0

An article with two figures created in Jupyter Notebooks. Each figure can be labeled directly in the notebook and reused in any other page directly.

Figure reused from [mystmd.org](https://mystmd.org) (CC-BY-4.0, [source](https://mystmd.org/guide/reuse-jupyter-outputs#reuse-jupyter-outputs)).
:::

 -->

<!-- For example, the following figure is the output of the `content/fig_1.ipynb` notebook:

:::{figure} #fig1cell
:label: fig1

An example of a figure generated from a Jupyter Notebook that lives in the `content` folder of this repository. Check `content/figure_1.ipynb` to see how this figure was generated and where the label `#fig1cell` is defined.
:::

Here is another figure generated from another notebook:

:::{figure} #fig2cell
:label: fig2

An example of a figure generated from a Jupyter Notebook that lives in the `content` folder of this repository.  Check `content/figure_2.md` to see how this figure was generated and where the label `#fig2cell` is defined.
:::

Both interactive, cool right! All your assets are centralized in this one document, which ideally lives in a GitHub repository. You may forget what you did, but your commit history will be there to remind you.

## NeuroLibre and MyST Markdown

NeuroLibre is a reproducible preprint publisher that makes it a seamless experience to publish preprints written in MyST Markdown, and commits to the long term preservation of the content, runtime, data, and the functionality of the code.

:::{seealso}
You can refer to [this blogpost](https://conp.ca/about-neurolibre/#:~:text=NeuroLibre%20is%20a%20platform%20for,articles%2C%20tutorials%2C%20and%20reports) for more information about NeuroLibre.
:::

### Data

Unless your preprint does not include any output that requires computational resources, you typically need to provide a set of inputs to supplement the generation of the assets in your article. The type and size of the data can vary greatly from one article to another, from a `50KB` excel spreadsheet to a `2GB` neuroimaging dataset of brain images.

The only requirement is that the data must be publicly available to be accessed by NeuroLibre. To specify your data dependencies, you can provide a `binder/data_requirement.json` file in the root of your repository, with the following structure:

```json
{
  { "src": "https://drive.google.com/uc?id=1hOohYO0ifFD-sKN_KPPXOgdQpNQaThiJ",
  "dst": "../data",
  "projectName": "neurolibre-demo-dataset"
  }
}
```

:::{note}
The above configuration specifies that the data will be downloaded from Google Drive and placed in and saved in a `data/neurolibre-demo-dataset` at the root of your repository. The `dst` field indicates `../data` as the root of the repository is one directory up from the `binder` directory where the `data_requirement.json` file is located.

Even when the `dst` field is specified differently, NeuroLibre will always mount the data in the `data` folder at the root of your repository. We recommend you to follow the same convention while working locally and to remember to `.gitignore` the `data` folder!
:::

:::{seealso}
You can refer to [this documentation](https://docs.neurolibre.org/en/latest/STRUCTURE.html#the-binder-folder-data) for more information about the `binder/data_requirement.json` file and the available options to specify your data dependencies.
:::

#### How can I get NeuroLibre to cache my data dependencies? 

You can use [this issue template](https://github.com/neurolibre/info/issues/new?assignees=agahkarakuzu&labels=DOWNLOAD&projects=&template=data_cache.md&title=) to request the caching of your data dependencies.

### Code 

NeuroLibre follows the [reproducible runtime environment specification (REES)](https://repo2docker.readthedocs.io/en/latest/specification.html) to define a runtime environment for your preprint. Any programming language supported by Project Jupyter (e.g. python, R, julia, etc.) can be used to create your executable content, where you place necessary [BinderHub configuration files](https://mybinder.readthedocs.io/en/latest/using/config_files.html#config-files) in the `binder` folder.

#### How much computational resources are available and for how long my notebooks can run to generate the outputs?

For each preprint, we guarantee a minimum of 1 CPU core and 4 GB of RAM (8GB maximum), and a maximum of 1 hours of runtime to execute all the notebooks in the `content` folder.

> Do you really want someone to run your code for 1 hour? Probably not.

Even though long-running code cells may be of interest to interactive tutorials, a reader who is interested in reproducing your Figure would be less likely to wait for more than a few minutes for the outputs to be generated. This is why we encourage you to create notebooks that can be run in the "attention span" of a reader.

### Preview your preprint

#### Locally

It is always a good practice to be able to build your MyST article locally before publishing it to NeuroLibre. If you install MyST as described [here](https://mystmd.org/guide/installing), in a virtual environment that has all your code dependencies installed, you can build your myst article:

```bash
cd path/to/your/repo
myst build --execute --html
```

:::{note}
NeuroLibre also supports Jupyter Book for publishing preprints. You can refer to [this documentation](https://jupyterbook.org/en/stable/intro.html) to find out more about it. However, as of late 2024, MyST is our recommended route for writing preprints.
:::

#### Roboneuro preview service

If you have a data dependency and have NeuroLibre cached it for you, you can start using the Roboneuro preview service to build your preprint: https://robo.neurolibre.org

#### Technical screening

Once you submit your preprint to NeuroLibre, our team will perform a technical screening to ensure that your preprint can be built successfully. This is to make sure that your preprint is in line with our guidelines and to avoid any issues that may arise during the build process.

You can visit our technical screening repository [neurolibre/neurolibre-reviews](https://github.com/neurolibre/neurolibre-reviews/issues) to see examples of this process.

### After your preprint is published

We archive all the reproducibility assets of your preprint on Zenodo and link those objects to your reproducible preprint that is assigned a DOI and indexed by [Crossref](https://www.crossref.org/) (also by Google Scholar, Researchgate, and other platforms that use Crossref metadata).

Your preprint can be found, cited, and more importantly, reproduced by any interested reader, and that includes you (probably a few years after you published your preprint)!

### Is the idea of wanting to publish a dashboard with your preprint too crazy?

Absolutely not! We encourage you to publish your dashboard alongside your preprint to showcase your results in the best way possible.

:::: {admonition} An interactive dashboard developed with R Shiny
:class: tip
:::{iframe} https://shinybrain.db.neurolibre.org
:width: 100%
:label: intdashboard
:align: center

MRShiny Brain interactive dashboard at [https://shinybrain.db.neurolibre.org](https://shinybrain.db.neurolibre.org)
:::
::::

:::: {admonition} An award-winning dashboard developed using Plotly Dash
:class: tip
:::{iframe} https://rrsg2020.db.neurolibre.org/
:width: 100%
:label: intdashboard2
:align: center

ISMRM RRSG 2020 interactive dashboard at [https://rrsg2020.db.neurolibre.org/](https://rrsg2020.db.neurolibre.org/)
:::
::::

These dashboards [](#intdashboard) and [](#intdashboard2) are embedded in their respective NeuroLibre preprints! If you are interested in publishing your own dashboard with NeuroLibre, please open an issue using [this template](https://github.com/neurolibre/info/issues/new?assignees=agahkarakuzu&labels=dashboard&projects=&template=new_dashboard.md&title=%5BNEW+DASHBOARD%5D).

If you have any questions or need further assistance, please reach out to us at `info@neurolibre.org`. --> -->
