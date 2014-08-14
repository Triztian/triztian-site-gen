title: Git Commands
author: Tristian Azuara
date: 2014-08-07
modified: 2014-08-07
slug: git-commands
summary: Simple one-liners of git and bash commands.
tags: git,bash,cli
category: development
thumbnail: http://www.git-scm.com/images/logo@2x.png

If you use git as your version control tool and have ever needed to use it in
an unusual way here I will list uses that took me more than 10 mins of reading
until I found a solution.

If you're new to git here is an excelent resource: [http://www.git-scm.com/](http://www.git-scm.com/)

### Last commit message text

    :::bash
    git log | grep '^\s\s*' | head -n1
