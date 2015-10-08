Title: Pop Quiz: Spot the Bug, CRON Edition
Date: 2010-04-01 04:47
Author: Bryce
Tags: cron, u\*nx
Slug: pop-quiz-spot-the-bug-cron-edition

That's right boys & girls, its quiz time. Get out your brains and
prepare to use them.

The file below is a standard cronjob file, hiding in /etc/cron.d. Can
anyone point out to me what the bug is? Assume that some_script exists
and produces output. And yes there is a bug in there. I promise.

```bash
55 14 * * * root sleep $(($RANDOM % 60)); logger -p local3.info "some script";
    OUT=`/opt/sbin/some_script 2>&1` ; logger -p local3.info $OUT;
```

Unless someone posts a comment with the correct answer( and earns
themselves a virtual beer), I will share the answer next week.
