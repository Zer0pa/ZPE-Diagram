# Publication Boundary Report

## Purpose

This document defines the local publication boundary prepared for repo-orchestrator review.

## Extracted Surface

The new repo contains only the bounded diagram product surface:

- SVG ingestion for line-based diagram inputs
- structural quantization into eight-direction stroke paths
- bounded style encoding for the frozen 8-color palette plus quantized stroke width
- preserved stroke ordering as explicit state
- standalone validation and focused tests for that bounded claim

## Included Public Material

- the vendored diagram modules required to parse, quantize, pack, and unpack the public word stream
- a standalone `DiagramEncoder` facade with bounded scope validation
- a reproducibility script and committed validation result
- repo-local docs, workflows, and packaging required by the playbook

## Intentionally Left Behind

The following were not extracted into `zpe-diagram`:

- any shared-core narrative or dependency chain
- non-diagram modality code
- research-wave naming and methodology framing
- fill semantics
- dash semantics on the encode path
- taper, pressure, and broader authorial-style claims
- out-of-palette color identity

## zpe-core Dependency Boundary

`zpe-diagram` does not depend on `zpe-core` as a public runtime dependency.

The public repo vendors its own diagram modules and its own minimal word-format constants so that a fresh clone can install and run without any shared platform claim.

## Review Notes

- the local predecessor workspace still contains the source diagram modules that were vendored here
- no removal edits were applied to the predecessor workspace during this preparation step
- repo-orchestrator review should decide whether any later cleanup inside the predecessor workspace is still needed

