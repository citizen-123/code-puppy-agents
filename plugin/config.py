# Skill trigger patterns and configuration for the superpowers plugin.
# Maps user intent patterns to skills/agents.
#
# Matching rules:
# - "strong" patterns match anywhere and are sufficient alone
# - "weak" patterns require the match to appear at the start of the message
#   (first 80 chars) to reduce false positives
# - "negative" patterns cancel a match if present anywhere in the message

SKILL_TRIGGERS = {
    "brainstorming": {
        "agent": "brainstormer",
        "strong": [
            "let's brainstorm",
            "help me design",
            "let's design",
            "I need to design",
        ],
        "weak": [
            "let's build",
            "let's create",
            "let's make",
            "I want to build",
            "I want to create",
            "new feature",
            "add a feature",
        ],
        "negative": [
            "let's build on",
            "let's build from",
            "let's create a plan",  # that's writing-plans
            "let's make a plan",    # that's writing-plans
            "continue",
            "keep going",
            "as I was saying",
        ],
        "description": "Collaborative design refinement before implementation",
        "announce": "Using brainstorming to explore and refine the design before implementation.",
    },
    "systematic-debugging": {
        "agent": "debugger",
        "strong": [
            "debug this",
            "fix this bug",
            "investigate this",
            "troubleshoot",
            "help me debug",
        ],
        "weak": [
            "why is this failing",
            "not working",
            "error when",
            "exception in",
            "crash when",
            "track down",
        ],
        "negative": [
            "broken into",
            "broken down",
            "broken up",
            "not working on that",
            "error when I tried to explain",
        ],
        "description": "Methodical hypothesis-driven debugging",
        "announce": "Using systematic-debugging to methodically isolate the root cause.",
    },
    "writing-plans": {
        "agent": "plan-writer",
        "strong": [
            "write a plan",
            "create a plan",
            "create an implementation plan",
            "make a plan",
            "write an implementation plan",
        ],
        "weak": [
            "implementation plan",
            "break this down into tasks",
            "plan this out",
            "decompose this",
        ],
        "negative": [
            "execute the plan",
            "follow the plan",
            "run the plan",
            "the plan is",
            "our plan was",
        ],
        "description": "Break approved designs into bite-sized implementation tasks",
        "announce": "Using writing-plans to create a detailed implementation plan.",
    },
}

# Skills that are behavioral guidelines (not dispatchable agents).
# Agents read these via read_file when relevant.
REFERENCE_SKILLS = [
    "test-driven-development",
    "using-git-worktrees",
    "finishing-a-development-branch",
    "requesting-code-review",
    "receiving-code-review",
    "dispatching-parallel-agents",
    "subagent-driven-development",
]

# Absolute base path for installed skills.
SKILLS_BASE = "~/.code_puppy/skills"
