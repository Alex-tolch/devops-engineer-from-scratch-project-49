# Brain Games

A set of simple CLI games: answer three questions in a row to win. Games include **brain-even** (is the number even?), **brain-calc** (result of an expression), **brain-gcd** (greatest common divisor), **brain-progression** (missing number in a sequence), **brain-prime** (is the number prime?).

## Requirements

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Alex-tolch/devops-engineer-from-scratch-project-49.git
cd devops-engineer-from-scratch-project-49
```

With **uv**:

```bash
uv sync
```

With **pip**:

```bash
pip install -e .
```

## Usage

Run a game (with uv):

```bash
uv run brain-games      # welcome only
uv run brain-even       # even/odd
uv run brain-calc       # arithmetic
uv run brain-gcd        # GCD
uv run brain-progression # progression
uv run brain-prime      # prime number
```

Or use **Make**:

```bash
make brain-games
make brain-even
make brain-calc
make brain-gcd
make brain-progression
make brain-prime
```

After a global install (`make build` then `make package-install`), you can run `brain-even`, `brain-calc`, etc. directly.

---

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Alex-tolch/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Alex-tolch/devops-engineer-from-scratch-project-49/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Alex-tolch_devops-engineer-from-scratch-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Alex-tolch_devops-engineer-from-scratch-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Alex-tolch_devops-engineer-from-scratch-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Alex-tolch_devops-engineer-from-scratch-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Alex-tolch_devops-engineer-from-scratch-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Alex-tolch_devops-engineer-from-scratch-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=Alex-tolch_devops-engineer-from-scratch-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=Alex-tolch_devops-engineer-from-scratch-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Alex-tolch_devops-engineer-from-scratch-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Alex-tolch_devops-engineer-from-scratch-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Alex-tolch_devops-engineer-from-scratch-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Alex-tolch_devops-engineer-from-scratch-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Alex-tolch_devops-engineer-from-scratch-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Alex-tolch_devops-engineer-from-scratch-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Alex-tolch_devops-engineer-from-scratch-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=Alex-tolch_devops-engineer-from-scratch-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Alex-tolch_devops-engineer-from-scratch-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Alex-tolch_devops-engineer-from-scratch-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Alex-tolch_devops-engineer-from-scratch-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Alex-tolch_devops-engineer-from-scratch-project-49)

## Demo

### brain-even
![brain-even demo](images/even-demo.gif)

### brain-calc
![brain-calc demo](images/calc.gif)

### brain-gcd
![brain-gcd demo](images/gcd.gif)

### brain-progression
![brain-progression demo](images/prog.gif)

### brain-prime
![brain-prime demo](images/prime.gif)
