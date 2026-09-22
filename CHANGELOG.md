# Journal des modifications

## Séance du mardi — passage en fiche de coaching terrain

### Vidéos découpées

Chaque vidéo utilisée dans `seance-mardi.html` a été revue image par image, puis découpée
en séquences réelles. Les images ne sont **jamais** prises à intervalles réguliers : elles
sont choisies une par une pour ce qu'elles montrent.

| Vidéo | Durée | Découpage retenu | Images extraites |
|---|---|---|---|
| `DbUqh3jRoQw_ryanyayawalker.mp4` | 35 s | 2 exercices. Ex. 1 = plan continu 11,5–16,5 s (une joueuse, ballon au-dessus de la tête, fente très basse). Ex. 2 = dip dynamique au plot, 26–31 s | `DbUqh3jRoQw_ex1_1..4.jpg`, `DbUqh3jRoQw_ex2_1..4.jpg` |
| `2rOdrFzcNls_@dhflagfootball.mp4` | 13 s | 3 tracés : slant (≈ 0,5–3 s), out (≈ 4–6,5 s), go (≈ 7,5–9,5 s) | `2rOdrFzcNls_slant_1..3.jpg`, `2rOdrFzcNls_out_1..3.jpg`, `2rOdrFzcNls_go_1..3.jpg` |
| `DdFXgBFvyGk_flaglabperformance.mp4` | 20 s | Montage de 8 plans courts. Seul le dernier plan (17–19,9 s) contient la séquence complète et lisible | `DdFXgBFvyGk_1..3.jpg` |
| `DcumOOqNKAi_issa_rantbro.mp4` | 36 s | Montage de prises du même atelier « Footwork ». Séquence continue la plus lisible : 12,4–18,9 s | `DcumOOqNKAi_1..4.jpg` |

Toutes les images sont en 480 px de large, extraites du fichier local du dépôt avec ffmpeg.

### Corrections de contenu

- **Le rusher n'est pas dans la vidéo QB.** `2rOdrFzcNls` montre un drill QB / receveur à
  trois ballons (slant, out, go) : aucun rusher à l'écran. Le rusher est signalé dans un
  encadré séparé comme **adaptation Iguanes**, et non comme le contenu de la référence.
- **Le flag pull n'est jamais montré jusqu'au bout.** Dans `DdFXgBFvyGk`, le plan coupe au
  moment où la main du défenseur arrive sur la ceinture : on ne voit jamais le fanion se
  détacher (vérifié image par image à 30 i/s). La fiche s'arrête donc à « main vers le
  flag », avec une note explicite.
- **L'atelier appuis est sans ballon.** `DcumOOqNKAi` est un travail d'appuis et de
  déplacement ; aucune consigne ne mentionne le ballon.
- `DdWjv_yla39_xypxox` est **retirée** de la séance du mardi (elle reste dans la galerie).

### Structure de la page

- Warm-up 15 min en trois temps : 0–5 préparation, 5–10 préparer le dip, 10–15 dip en mouvement.
- Technique : schéma des **2 circuits identiques** (QB fixe, zone QB, zone Flag pull, sas
  appuis) puis **3 fiches de coaching** : zone QB (3 tracés), zone Flag pull, appuis / sortie.
- Chaque fiche : nom, objectif, chaîne visuelle, images extraites légendées, 2–3 consignes
  essentielles, bouton vidéo calé sur la séquence, et un repli « Détails coaching »
  (déroulement complet, points de coaching, erreurs à éviter).
- Renforcement : finisher collectif (squats 100, pompes 50, abdos 100, gainage 10 s × joueurs)
  à la place de l'AMRAP.

## Clarification opérationnelle de la rotation

Passe de clarification uniquement : aucun design refait, aucune fiche vidéo reconstruite.

- **Rotation corrigée.** Les 4 joueurs de chaque circuit forment **2 binômes**. Le binôme en
  zone QB reste pour un **mini-set complet** — slant → out → go, soit **3 passes**, le rusher
  pressant les trois. Le binôme en zone Flag pull fait **4 reps** (2 attaques + 2 défenses par
  joueur, inversion à chaque rep). Ensuite **les deux binômes échangent de zone**.
- **Formule ambiguë supprimée** : « chacun change de rôle après chaque passage » disparaît au
  profit de « Les QB restent fixes. Les deux binômes échangent de zone après chaque mini-set complet. »
- **Nouveau bloc « Quand on tourne ? »** sous le schéma : zone QB = slant + out + go terminés,
  zone flag = 4 reps terminées → les deux binômes échangent. Visible sans ouvrir les détails.
- **Sas appuis renforcé** dans le schéma : un joueur après l'autre, quelques secondes,
  « pas de file, pas d'attente ». Ce n'est pas une troisième station.
- **Renforcement** : les volumes sont présentés comme des **objectifs totaux** (100 squats,
  50 pompes, 100 abdos) avec **4 tours conseillés** (25 / 12-13 / 25).
- **Gainage reformulé** : tout le groupe reste en gainage pendant que chaque joueur compte
  10 secondes à voix haute, à tour de rôle — 10 joueurs = 1 min 40 de gainage continu, personne n'attend.

## Bouton vidéo plus visible

Les boutons « Voir dans la vidéo » passent en plein accent : fond vert, texte contrasté,
police plus grande et plus grasse, icône lecture agrandie. Les trois boutons de tracé
(0:01 / 0:04 / 0:08) restent volontairement discrets, en simple contour accent, pour ne pas
concurrencer le bouton principal de chaque fiche.

## Clarification terrain : binômes, déclencheur de rotation, finisher

- **Confusion A/B levée.** Les zones redeviennent neutres (`Zone QB`, `Zone Flag pull`) : ce
  sont les binômes qui tournent, pas les zones. Un bloc dédié affiche l'échange :
  **Binôme A — Zone QB → Zone Flag pull** et **Binôme B — Zone Flag pull → Zone QB**.
- **Inversion des rôles en zone QB.** À chaque retour d'un binôme dans la zone, le receveur et
  le rusher **inversent leurs rôles** — personne ne reste toujours receveur ou toujours rusher.
- **Le mini-set QB devient le déclencheur de rotation.** Le flag pull n'a plus de quota rigide :
  il enchaîne les reps **en continu** jusqu'au signal du QB (≈ 4 reps par mini-set, sans jamais
  ralentir pour atteindre un chiffre). Au signal, on termine la répétition en cours et les deux
  binômes échangent.
- **Sas appuis** : règle terrain explicite — flag pull terminé → joueur 1 traverse → joueur 2
  traverse → retour zone QB. Un par un, pas de file, pas d'attente.
- **Finisher corrigé** : `4 × 12 ou 13 pompes = 50` était faux. Remplacé par
  **Pompes : 12 / 13 / 12 / 13** (12 + 13 + 12 + 13 = 50). Squats 25 × 4 = 100 et abdos
  25 × 4 = 100 inchangés.

## Micro-corrections de cohérence

- **Binômes renommés 1 et 2** pour ne plus confondre avec les circuits : `Circuit A` / `Circuit B`
  restent, mais les binômes deviennent **Binôme 1** et **Binôme 2** (une seule lettre A/B dans la page).
- **Formulation du Flag pull corrigée** : « environ 4 reps… idéalement une fois chacun » était
  incohérent avec l'inversion à chaque rep. Remplacé par : « reps en continu jusqu'au signal QB ;
  inversion à chaque rep ; viser ≈ 4 reps, soit ≈ 2 dans chaque rôle par joueur ».

## Pack d'analyse vidéo (`analysis/`)

Nouvel outil de travail, **distinct de `thumbs/`** (rien n'est affiché sur le site).

- `./analyse-video` — niveau 1 : extrait **2 images/seconde** sur toute la vidéo (hauteur 720 px),
  les nomme `frame_0000_00.0s.jpg` (index + timestamp), génère des **planches contact de 12
  images** avec le timestamp incrusté sous chaque vignette (ordre chronologique strict), et
  écrit un `manifest.json` (durée, fps source, cadence, liste des frames et des planches).
- `./analyse-video-detail VIDEO 17 21 [fps]` — niveau 2 : **8 i/s** (réglable 5–10) uniquement
  sur la plage demandée, hauteur 900 px, mêmes planches et manifest.
- 25 vidéos traitées, soit ~1 650 images et ~140 planches.
- `analysis/README.md` décrit le workflow (planches → repérage des exercices → détail → choix
  des images à copier dans `thumbs/`).

Note : `drawtext` n'étant pas compilé dans le ffmpeg local, l'incrustation des timestamps est
faite avec ImageMagick (montage), et la locale est forcée en `C` pour que les timestamps
s'écrivent `00.0s` et non `00,0s`.

## Warm-up : la vidéo DIP passe de 2 à 5 exercices

L'ancien découpage (2 exercices) simplifiait trop `DbUqh3jRoQw`. Réanalyse complète à partir
du pack `analysis/` (planches 2 i/s puis détails à 10 i/s sur les passages clés) : la vidéo
montre une **progression de 5 exercices**, pas deux blocs génériques.

| # | Exercice | Prise retenue | Images |
|---|---|---|---|
| 01 | Mobilité basse — ballon au-dessus de la tête | 11,5 → 16,5 s | 13,30 / 13,60 / 14,50 / 15,10 |
| 02 | Dip explosif, mains derrière la tête | 8,4 → 10,5 s | 8,40 / 8,80 / 9,40 |
| 03 | Dip / cut avec ballon sécurisé | 22,0 → 24,4 s | 23,30 / 23,40 / 23,60 / 24,20 |
| 04 | Dip en mouvement — ballon au-dessus de la tête | 2,2 → 6,6 s | 2,30 / 3,50 / 5,60 / 6,20 |
| 05 | Feinte du corps et du ballon + changement de direction | 32,1 → 34,7 s | 32,60 / 33,10 / 33,50 / 33,80 |

Répartition des 15 minutes revue : 0–3 mobilité générale, 3–6 ex. 01, 6–8 ex. 02, 8–11 ex. 03,
11–13 ex. 04, 13–15 ex. 05.

- Chaque fiche garde la même première couche qu'avant : numéro, nom, chaîne, 3–4 images,
  3 consignes, bouton vidéo. Le déroulement, les points de coaching et les erreurs restent
  repliés dans **Détails coaching**.
- 19 nouvelles images dans `thumbs/` ; les 8 anciennes (`DbUqh3jRoQw_ex1_*`, `ex2_*`) sont
  supprimées, elles ne correspondaient plus au découpage.
- Registre vidéo mis à jour : `mob` 11,5 s · `noball` 8,4 s · `cut` 22,0 s · `move` 2,2 s ·
  `fake` 32,1 s (les clés `ex1`/`ex2` disparaissent). Les 11 popups ont été retestées.
- **Vérification honnête sur l'exercice 02** : la vidéo ne contient pas de séquence réellement
  « sans ballon » isolée. Sur la prise 8,4–10,5 s, une partie du groupe garde le ballon
  au-dessus de la tête et d'autres ont les mains derrière la tête — c'est le même drill. La
  fiche le dit explicitement et les images montrent une joueuse mains derrière la tête.
- Impression : 14 pages (contre 10), une fiche par page environ pour le warm-up.

## Warm-up : 4 exercices + 1 variante (au lieu de « 5 exercices »)

L'introduction annonçait « une progression de 5 exercices… ceux de la vidéo », ce qui contredisait
notre propre vérification : l'ancien exercice 02 (sans ballon) n'est pas un exercice distinct filmé,
c'est le **même drill que le 01**, avec une partie du groupe mains derrière la tête.

- Nouvelle présentation : **4 exercices issus de la vidéo + 1 variante de progression**.
  `01` Mobilité basse, ballon haut · `01B` Variante sans ballon, mains derrière la tête ·
  `02` Dip/cut avec ballon sécurisé · `03` Dip en mouvement, ballon haut · `04` Feinte corps + ballon.
- Introduction : « 15 min : 4 exercices issus de la vidéo + 1 variante de progression. Du contrôle
  bas jusqu'à la feinte en situation dynamique. »
- La fiche `01B` porte désormais « **Variante de l'exercice 01** » en tête d'objectif.
- Légendes vidéo et textes alternatifs des 19 images alignés sur la nouvelle numérotation.

## Fiche QB : images reprises depuis le pack d'analyse

Même méthode que pour la vidéo DIP : planches 2 i/s, puis vérification des candidats en pleine
résolution, image par image, avant de toucher à la fiche.

- **Slant** : 1,20 (départ, libellé « 1. SLANT » affiché) · 2,20 (le ballon quitte la main) ·
  2,90 (le receveur saute, bras levés).
- **Out** : 4,40 (face à face) · 5,30 (bras armé au-dessus de l'épaule) · 6,00 (ballon en vol
  vers la ligne). L'ancienne image de « cassure » (4,55) ne montrait ni cassure ni ballon.
- **Go** : 7,90 (alignés, libellé « 3. GO ») · 8,60 (bras armé) · 9,80 (ballon nettement en l'air).
- Repères des popups ajustés sur l'apparition des libellés : slant 1,0 s · out 4,0 s · go 7,5 s
  (bouton passé de ▶ 0:08 à ▶ 0:07).
- Deux affirmations retirées faute de preuve à l'image : « ballon attrapé en avançant » (le ballon
  n'est pas lisible dans les mains) et « réception près de la ligne, pieds dedans ».
- Vérifié au passage : le libellé du 2ᵉ tracé est bien **« 2. OUT »** du début à la fin (une lecture
  de planche m'avait fait croire à « 2. CUT » : c'était un artefact de compression).
- Aucun rusher dans la vidéo, et le QB tient bien deux ballons dans les mains à 4,80 s : le
  « 3-ball drill » du titre est littéral.

## Fiche Flag pull : images reprises depuis le pack d'analyse

Même méthode : planches 2 i/s, repérage des 8 plans réels, puis vérification des candidats en
pleine résolution et **zoom sur la zone de contact** avant de toucher à la fiche.

Les 3 images précédentes venaient du **plan 8** (17,0–19,8 s) — le plus faible : contre-jour
relatif et échelle moyenne. Elles sont remplacées par 4 images prises dans les meilleurs plans :

| Image | Plan | Moment |
|---|---|---|
| Réaction | 6 (11,7–14,8 s), **12,00 s** | base large, hanches basses, attente du premier pas |
| Fermeture de l'angle | 7 (14,8–17,0 s), **16,20 s** | corps sur la trajectoire, bras qui part vers la hanche |
| Main vers le flag | 3 (3,7–6,4 s), **5,40 s** | approche basse, gant tendu vers le fanion jaune |
| Gant sur le flag | 3, **5,70 s** | le gant arrive sur le fanion, tiré sous tension |

**Correction d'une affirmation fausse de la fiche.** La note disait : « le plan coupe à l'arrivée
de la main ». C'est faux. Le zoom montre le gant qui part vers le fanion jaune (5,40 s), le gant
qui arrive dessus (5,70 s) et le **contact maintenu environ 0,7 s** (jusqu'à la coupe à 6,37 s),
le fanion visiblement tiré. En revanche, **aucune image ne montre le fanion se détacher** : c'est
cette partie-là qui est à travailler à part. La note dit maintenant exactement cela.

- Bouton vidéo recalé sur le plan clé : **4,8 s** au lieu de 17,2 s (bouton passé de · 18 s à · 5 s).
- Grille passée de 3 à 4 images (`.frames`) pour montrer à la fois l'approche et la saisie.
- Affiche de galerie `thumbs/DdFXgBFvyGk_flaglabperformance.jpg` : supprimée par erreur pendant
  la génération, restaurée à l'identique depuis git (vérifié : identique à HEAD).

## Fiche Appuis : images reprises depuis le pack d'analyse

Même méthode : planches 2 i/s, repérage des 6 prises réelles, vérification des candidats en
pleine résolution.

Les 4 images précédentes venaient de **3 prises différentes** (6,40 / 15,30 / 16,80 / 18,60 s).
Elles sont remplacées par 4 images issues d'**une seule prise continue** — la meilleure
(prise 2, 6,2–12,5 s : sujet le plus grand, le mieux éclairé, même joueur du début à la fin) :

| Image | Moment |
|---|---|
| Entrée | **6,60 s** — le joueur arrive déjà en mouvement, hanches basses |
| Abaissement | **8,10 s** — les hanches descendent, un pied se pose sur la ligne |
| Appuis courts | **8,40 s** — position la plus basse, pieds rapprochés, buste replié |
| Sortie | **8,90 s** — poussée de la jambe arrière, le buste se redresse |

**Correction d'une affirmation fausse.** La légende « Entrée » disait : « le joueur entre déjà
lancé, **pas de départ arrêté** ». C'est faux : la prise 1 (0,00 → 0,90 s) montre un joueur
immobile, fléchi, mains près des genoux, presque une seconde avant le premier pas. Vérifié image
par image.

**Ajout d'une nuance honnête.** Le joueur de la vidéo **ne change pas de direction** : il croise
les appuis et tourne le buste le long de la ligne, sans inversion de trajectoire. La note le dit
maintenant explicitement, et précise que la **réorientation et la sortie vers le QB sont notre
adaptation** — pas le contenu de la source.

- Bouton vidéo recalé sur la meilleure prise : 6,2 s au lieu de 6,0 s (libellé · 6 s inchangé).
- Aucun ballon dans toute la vidéo : confirmé (les prises 5 et 6, en contre-jour, sont écartées).
