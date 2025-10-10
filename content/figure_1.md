---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# Figure 1: Interactive NeuroTmap Analysis

This figure shows the comparative analysis of neuroimaging sessions with overlay capabilities.

```{code-cell} python
:tags: [remove-input]
:label: fig1cell

from Dash_client import DashNeuroTmapClient

# Initialiser le client
client = DashNeuroTmapClient()

# Créer l'interface interactive
client.create_advanced_interface()
```