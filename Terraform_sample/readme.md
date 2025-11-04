# Environments Directory

This directory contains environment-specific configuration files and settings.

## Purpose
- Houses different environment configurations (e.g., development, staging, production)
- Manages environment-specific variables and settings
- Separates configuration concerns for different deployment scenarios

## Common Environment Types
- Development (dev)
- Staging/QA
- Production (prod)
- Testing

## Usage
Each environment folder typically contains configuration files that are loaded based on the current running environment of the application.

### Directory Structure
```
TERRAFORM/
├── envs/
│   ├── dev.tfvars
│   ├── test.tfvars
│   └── prod.tfvars
├── main.tf
├── provider.tf
├── variables.tf
└── outputs.tf
```

### Common Commands
```bash
terraform init
terraform fmt
terraform validate
terraform plan -var-file="envs/dev.tfvars"
terraform apply -var-file="envs/dev.tfvars" -auto-approve
terraform destroy -var-file="envs/dev.tfvars" -auto-approve
terraform show
```

Main commands:
  init          Prepare your working directory for other commands
  validate      Check whether the configuration is valid
  plan          Show changes required by the current configuration
  apply         Create or update infrastructure
  destroy       Destroy previously-created infrastructure

All other commands:
  console       Try Terraform expressions at an interactive command prompt
  fmt           Reformat your configuration in the standard style
  force-unlock  Release a stuck lock on the current workspace
  get           Install or upgrade remote Terraform modules
  graph         Generate a Graphviz graph of the steps in an operation
  import        Associate existing infrastructure with a Terraform resource
  login         Obtain and save credentials for a remote host
  logout        Remove locally-stored credentials for a remote host
  metadata      Metadata related commands
  modules       Show all declared modules in a working directory
  output        Show output values from your root module
  providers     Show the providers required for this configuration
  refresh       Update the state to match remote systems
  show          Show the current state or a saved plan
  stacks        Manage HCP Terraform stack operations
  state         Advanced state management
  taint         Mark a resource instance as not fully functional
  test          Execute integration tests for Terraform modules
  untaint       Remove the 'tainted' state from a resource instance
  version       Show the current Terraform version
  workspace     Workspace management
