# TEKUP-CTF-2024
This repository contains the challenges of Securinets TEK-UP CTF 2024


## Info

- Flag format: `Securinets{.*}`
  - `Securinets{test_flag}`
- Event duration: `12hrs`

## Add a challenge

# PLS DO NOT PUSH TO MASTER/MAIN MAKE PR FIRST

before you make ur changes

```
git branch <challenge>
```

```
git add .
git commit -m "<category>_<challenge_name>"
git push origin <challenge>
```
then you can visit the repo on your browser and you should find a button to make a pull request

## Challenge modif

using ctfcli we can update challenges easily (example: change description in challenge.yml file)

```
python3 -m ctfcli sync <challenge>
```
## Port range

- Misc: 1000 - 1500
- Web: 1500 - 3000
- Pwn:  6000 - 7000
- Crypto: 8000 - 9000

## Challenges

Quick overview over a challenges structure:

- `challenges/` - Challenges directory
  - `misc/` - category
    - `test-chal/` - challenge
      - `README.md` - description, notes.
      - `challenge.yml` - [Challenge metadata](https://github.com/CTFd/ctfcli/blob/master/ctfcli/spec/challenge-example.yml) 
      - `compose.yml` - docker compose 
      - `solution/` - directory with solver / writeup
      - `handout/` - directory with `{category}_{challenge_name}.7z` file that would be given to players


___

### Cryptography

| Name                | Difficulty  | Author            | Wave |
|---------------------|-------------|-------------------|------|
| Prideful Revenge    | ?           |                   |      |


### Misc

| Name                        | Difficulty | Author         | Wave |
|-----------------------------|------------|----------------|------|
| Heimerdinger                | ?          |                |      |
| LEE SIN                     | ?          |                |      |
| PERMS                       | ?          |                |      |


### Forensics

| Name                 | Difficulty  | Author            | Wave |
|----------------------|-------------|-------------------|------|


### Pwn

| Name               | Difficulty | Author        | Wave |
|--------------------|------------|---------------|------|


### Reverse engineering

| Name            | Difficulty | Author | Wave |
|-----------------|------------|--------|------|


### Web

| Name               | Difficulty | Author          | Wave |
|--------------------|------------|-----------------|------|
| B17                | ?          |                 |      |
| reCURSED           | ?          |                 |      |
| Random Quotes      | ?          |                 |      |
| psyducklove        | hard       | j3seer          |      |

___

## Waves

### First

- +0h

### Second

- +6h

