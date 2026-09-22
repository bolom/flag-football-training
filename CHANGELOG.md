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
