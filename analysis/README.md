# Pack d'analyse vidéo — flag football

Ce dossier est un **outil de travail**, distinct de `thumbs/` (les images utilisées en
production sur le site). Rien ici n'est affiché par `seance-mardi.html` ni par la galerie.

Objectif : permettre d'analyser une vidéo de drill **image par image**, d'identifier les
exercices, leurs débuts et fins, et de comprendre les mouvements — sans revoir la vidéo
en boucle.

## Structure produite

```
analysis/
  <video-id>/
    frames/                 une image toutes les 0,5 s (2 i/s), hauteur 720 px
      frame_0000_00.0s.jpg  le nom contient l'index ET le timestamp exact
      frame_0001_00.5s.jpg
      ...
    sheets/                 planches contact de 12 images, timestamps incrustés
      sheet_01.jpg          ordre chronologique strict : gauche → droite, haut → bas
      sheet_02.jpg
      ...
    manifest.json           durée, fps source, cadence d'analyse, liste des frames
    detail_12-16_8fps/      (niveau 2) gros plan sur une plage de temps
      frames/ sheets/ manifest.json
```

## Niveau 1 — comprendre la vidéo

```bash
./analyse-video                          # toutes les vidéos de videos/
./analyse-video videos/ma-video.mp4      # une seule
```

Extrait **2 images par seconde** sur toute la vidéo, sans choix manuel : couverture
régulière. Une vidéo de 30 s donne ~60 images.

Ce qu'on lit dans les planches :

- changement d'exercice ;
- nouvelle répétition ;
- changement de position ou de joueur ;
- transition, début et fin d'une séquence.

## Niveau 2 — comprendre le mouvement

Quand une plage mérite plus de précision (placement du pied, descente des hanches,
changement d'appui, orientation des épaules, manipulation du ballon, sortie du mouvement) :

```bash
./analyse-video-detail videos/ma-video.mp4 17 21       # 8 i/s de 17 s à 21 s
./analyse-video-detail videos/ma-video.mp4 17 21 10    # 10 i/s
```

Le niveau 2 ne tourne **jamais** sur toute la vidéo : ce serait trop volumineux. On ne
l'utilise qu'après avoir repéré une zone intéressante au niveau 1.

## Comment s'en servir

1. Ouvrir le `manifest.json` pour connaître la durée, le fps source et le nombre de frames.
2. Regarder les planches `sheets/sheet_01.jpg`, `sheet_02.jpg`… dans l'ordre.
3. Noter les bornes de chaque exercice (elles sont lisibles directement : le timestamp est
   sous chaque image).
4. Demander une plage précise pour le détail :
   *« montre-moi les frames entre 12 et 16 secondes »* → les fichiers
   `frames/frame_00xx_12.5s.jpg` répondent directement, sans réextraire quoi que ce soit.
5. Si 2 i/s ne suffit pas → `./analyse-video-detail` sur la plage.
6. Choisir ensuite 3 à 5 images pédagogiques, et **copier seulement celles-là** dans
   `thumbs/` avec la convention `<video>_<sequence>_<n>.jpg`.

## Cadence et résolution

| | Niveau 1 | Niveau 2 |
|---|---|---|
| Cadence | 2 images/s | 8 images/s (réglable 5–10) |
| Couverture | toute la vidéo | une plage de quelques secondes |
| Hauteur | 720 px | 900 px |
| Planches | 12 images | 12 images |

Les images individuelles sont volontairement à 720 px : assez nettes pour voir les pieds,
les hanches, le ballon, les flags et l'orientation du corps, sans être énormes.

## Dépendances

`ffmpeg`, `ffprobe` (extraction) et ImageMagick (`magick`, pour les planches contact et
l'incrustation des timestamps — `drawtext` n'est pas disponible dans tous les ffmpeg).
