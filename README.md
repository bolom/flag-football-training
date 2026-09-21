# Extraction des vidéos Instagram

**En ligne : <https://bolom.github.io/flag-football-training/>** — la séance de mardi et la
galerie sont publiées depuis ce dossier via GitHub Pages. Le reste de ce document décrit
l'extraction d'origine des 23 vidéos Instagram.

Extraction réalisée le **21/09/2026** à partir des 23 liens fournis.

## Méthode

1. Instance Chrome lancée avec `--remote-debugging-port=9333` sur une **copie minimale**
   du profil (cookies + clé de chiffrement) — le Chrome principal n'a pas été touché.
2. Shortcode Instagram converti en `media_id` (base64url maison).
3. Appel de l'API interne `GET /api/v1/media/<media_id>/info/` depuis le contexte de la page
   (session et cookie CSRF de l'utilisateur), en-tête `x-ig-app-id: 936619743392459`.
4. Parcours récursif du JSON pour collecter toutes les clés `video_versions[].url`.
5. Téléchargement direct depuis le CDN `instagram.fptp4-1.fna.fbcdn.net`.

Résultat : **23/23 liens résolus, 0 erreur, 23 URLs uniques**.

## Fichiers

| Fichier | Contenu |
|---|---|
| `urls-video.txt` | Les 23 URLs vidéo, une par ligne |
| `urls-video.json` | URLs + métadonnées (shortcode, compte, légende, dimensions) |
| `urls-video.tsv` | Tableau lisible : shortcode / compte / résolution / URL |
| `manifeste.txt` | Inventaire des fichiers téléchargés |
| `videos/` | Les fichiers `.mp4` (les 23 extractions Instagram + les vidéos téléchargées depuis X, YouTube…) |
| `preview.html` | Galerie de prévisualisation locale (fichier généré, à ouvrir directement) |
| `preview.template.html` | Gabarit de la galerie, avec le marqueur `__DATA__` |
| `build-preview.py` | Régénère `preview.html` + les vignettes manquantes |
| `thumbs/` | Une vignette JPG par vidéo (480 px de large) |
| `seance-mardi.html` | Feuille de séance de 2 h (blocs, circuit technique en parcours, AMRAP) |

## Aperçu

En ligne : <https://bolom.github.io/flag-football-training/> (`index.html` sert de sommaire).
En local, ouvrir `preview.html` dans un navigateur (double-clic — le `file://` est
volontaire : un serveur HTTP Python ne gère pas les requêtes `Range`, donc le défilement
dans les vidéos serait cassé).

Fonctions : recherche, filtre par compte, tri, filtre « non vues », densité des
vignettes, thème clair/sombre, visionneuse avec navigation clavier
(`←` `→` `Espace` `M` `F` `Échap`) et reprise de lecture mémorisée par vidéo.

Après ajout ou suppression de `.mp4` dans `videos/`, régénérer :

```bash
python3 build-preview.py
```

## Important — expiration

Les URLs CDN sont **signées et temporaires** : elles expiraient le **22/09/2026 entre
20h28 et 23h48**, soit environ 32 h après l'extraction. Les fichiers `.mp4` du dossier
`videos/` sont donc la copie durable ; les URLs de `urls-video.txt` ne sont plus valides
passé ce délai et devront être régénérées.

## Inventaire

```
SHORTCODE        COMPTE                     DUREE    RESOLUTION  TAILLE    FICHIER
DcHC2HbSsEt      flagfootballedge           15      s 720x1280    3.5M      videos/DcHC2HbSsEt_flagfootballedge.mp4
DYZ1Y-_IK6V      jenny.flagfootball         52      s 720x1280     22M      videos/DYZ1Y-_IK6V_jenny.flagfootball.mp4
DcumOOqNKAi      issa_rantbro               36      s 720x1280     13M      videos/DcumOOqNKAi_issa_rantbro.mp4
DbUqh3jRoQw      ryanyayawalker             35      s 720x1280     21M      videos/DbUqh3jRoQw_ryanyayawalker.mp4
Db8QeafsCGn      nextlevelculture           17      s 720x1280    2.7M      videos/Db8QeafsCGn_nextlevelculture.mp4
DcylBuQsR8X      gym_cumados                22      s 720x1280    2.7M      videos/DcylBuQsR8X_gym_cumados.mp4
DbB4reFhmqc      nextlevelculture           25      s 720x1280    8.6M      videos/DbB4reFhmqc_nextlevelculture.mp4
Dc07nD9IWIQ      bala.training              34      s 720x1280    6.9M      videos/Dc07nD9IWIQ_bala.training.mp4
DdWjv_yla39      xypxox                     7       s 720x1280    1.6M      videos/DdWjv_yla39_xypxox.mp4
DbqgFBStgE0      martamathews_              18      s 720x1280    4.6M      videos/DbqgFBStgE0_martamathews_.mp4
DZ-4EngPvRy      andreapetrone_             68      s 720x1280     29M      videos/DZ-4EngPvRy_andreapetrone_.mp4
Dc1OYpMtbvT      martamathews_              14      s 720x1280    6.0M      videos/Dc1OYpMtbvT_martamathews_.mp4
DcJ-RFEhSw8      im22fitness                8       s 720x1280    2.1M      videos/DcJ-RFEhSw8_im22fitness.mp4
DcjO5jbgQqt      flyte_club                 27      s 720x1280     14M      videos/DcjO5jbgQqt_flyte_club.mp4
DdFXgBFvyGk      flaglabperformance         20      s 720x1280    8.8M      videos/DdFXgBFvyGk_flaglabperformance.mp4
DdKaCQbBNt4      toribrito6                 14      s 720x1280    1.7M      videos/DdKaCQbBNt4_toribrito6.mp4
Dc4wl_kNWXy      flagfootballedge           31      s 720x1280    8.6M      videos/Dc4wl_kNWXy_flagfootballedge.mp4
DYGDo_ZtiU4      flagfootball_ducks         27      s 720x1280     17M      videos/DYGDo_ZtiU4_flagfootball_ducks.mp4
Dczym60zlH0      colleenaugustinmma         139     s 720x1280     53M      videos/Dczym60zlH0_colleenaugustinmma.mp4
Dc8BDb7N9qM      womensflagfootballcamp     11      s 720x1280    7.3M      videos/Dc8BDb7N9qM_womensflagfootballcamp.mp4
Dc_kBkJxAHC      gridirongangfootball       89      s 720x1280     23M      videos/Dc_kBkJxAHC_gridirongangfootball.mp4
Dc3ZbmWo4-D      jenny.flagfootball         48      s 720x1280     22M      videos/Dc3ZbmWo4-D_jenny.flagfootball.mp4
DbWcwdaSAIa      football_phenoms           31      s 720x1280     12M      videos/DbWcwdaSAIa_football_phenoms.mp4
```

Toutes les vidéos sont en **720x1280** (vertical), encodage H.264/AAC dans un conteneur MP4.

### Vidéos d'autres sources

Une vidéo téléchargée ailleurs (X, YouTube, TikTok…) se pose simplement dans
`videos/`, accompagnée d'un fichier `<même nom>.json` qui porte ses métadonnées :

```json
{
  "id": "2101676087222964545",
  "title": "Tw93 — démo Mole",
  "uploader": "Tw93",
  "uploader_id": "@HiTw93",
  "url": "https://x.com/HiTw93/status/2101676087222964545",
  "upload_date": "2026-09-20",
  "thumb_at": 9
}
```

`thumb_at` (secondes, optionnel) choisit l'instant de la vignette — utile quand les
premières secondes sont un fondu ou un écran noir. Sans sidecar, le script retombe sur
`urls-video.json`, puis sur le nom de fichier. Les vidéos non verticales sont posées
entières sur un fond flouté pour garder la grille homogène.
