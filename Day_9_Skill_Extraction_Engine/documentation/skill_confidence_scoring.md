# Skill Confidence Scoring

## Objective

The Skill Extraction Engine assigns a confidence score to every
identified skill to indicate how reliably the skill was detected.

## Confidence Logic

The base confidence score starts at 0.80.

Additional confidence is added when:

- The detected skill exactly matches the canonical skill name.
- The skill appears in a skills-related context.
- The detected skill is identified from a recognized technology stack.

## Score Range

Confidence scores are maintained between 0.00 and 0.99.

### Examples

| Detection Type | Confidence |
|---|---:|
| Exact skill match | 0.90 |
| Skill in relevant context | 0.98 |
| Skill stack expansion | 0.85 |
| Synonym match | 0.80+ |

## Normalization

Different names referring to the same skill are mapped to a
single canonical skill.

Examples:

- Python / Py → Python
- JavaScript / JS → JavaScript
- React / ReactJS / React.js → React
- NLP → Natural Language Processing
- LLM / LLMs → Large Language Models

## Skill Stack Handling

Common technology stacks are expanded into their individual
skills.

Example:

MERN → MongoDB, Express.js, React, Node.js

MEAN → MongoDB, Express.js, Angular, Node.js

## Deduplication

If the same skill appears multiple times in a resume, it is
stored only once in the final structured output.

## Output

Each extracted skill contains:

- Skill name
- Category
- Confidence score
- Matched text

This structured information can be used by downstream ATS,
screening, and candidate-matching systems.