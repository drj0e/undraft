---
title: "The Old Name Still Answers"
date: 2026-10-08
draft: false
tags: ["data", "ai-tooling"]
shape: note
origin: thread
reach: core
summary: "The safe way to rename a column keeps the old name alive as an alias until the last consumer moves. For a reader that binds to names, the alias is a second column with the stale meaning, and the rename isn't done until the step most shops never schedule."
reviewed: true
---

```sql
CREATE VIEW samples AS
  SELECT id, released_count AS available_sample FROM specimens;
```

That view is what the safe way to rename a column leaves behind. [Parallel change](https://martinfowler.com/bliki/ParallelChange.html), expand and contract, breaks an incompatible change into three phases: add the new interface, move the consumers, remove the old one. The [strong_migrations](https://github.com/ankane/strong_migrations) gem spells the column version out in six steps, and the sixth is drop the old column. Between the first step and the sixth, both names answer.

A month ago I argued that meaning belongs in the [column name](/posts/printed-on-the-tube/), because a name can be renamed and a key can't. I still think so. What I skipped is that the rename procedure every migration guide recommends is, for most of its life, a procedure for keeping the old name alive. The view above is the expand phase. The old meaning is still selectable, and it still matches the words in the question.

For a person reading the catalog, the alias is plumbing. For an agent that [binds to the name](/posts/agents-dont-read-the-glossary/), the alias is a second column, and often the closer match, because the plain name is usually the old one. That's why it got picked, and why it misled. Nothing in the agent's path separates a column from a view that exists in order to be deleted.

So the rename finishes at contract, the phase that breaks whatever still used the old name. Expand is a migration with a diff and a reviewer. Contract is a deprecation, and it waits on the same proof every deprecation waits on: that the last consumer has moved. Checking that means reading every query that touches the table, or dropping the view and waiting for the page.

You can comment the view as deprecated. That's the glossary entry again, written for the reader who skips it.

Count the views in your warehouse whose only job is keeping an old column name answering. Each one is a definition the steward retired on paper and the schema kept live.
