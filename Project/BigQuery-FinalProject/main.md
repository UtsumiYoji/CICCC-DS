# Final Project: Tsunami & Earthquake Analytics with BigQuery

## Introduction

### My interset

Tsunami and Earthquake are common natural disasters in few countries like Japan, Turkey, France. I would like to figure out how serious these damages and make sure Japan is called earthquake country. I wondered Japan turly got a lot of damage more than other countires.

### My dataset

- Significant Earthquakes Database
  - Provided by NOAA in google public dataset
  - https://console.cloud.google.com/bigquery(cameo:product/noaa-public/noaa-earthquakes)

## Analyze

### Data cleaning

#### Significant Earthquakes Database

First of all, I didn't need data which didn't have `eq_primary` or `country`. eq_primary express how earthquak was big. And also, this dataset included BC data, this time, I wanted to focus on AD.

```sql
SELECT *
FROM `bigquery-public-data.noaa_significant_earthquakes.earthquakes`
WHERE eq_primary IS NOT NULL
AND country IS NOT NULL
AND year > 0;
```

### Exploring

#### What country had most number of earthquakes

First, I looked up what country had most nmber of earthquakes.

```sql
SELECT country, COUNT(*) as num
FROM `ciccc-lab.final_project.cleaned_earthquakes`
GROUP BY country
ORDER BY num DESC
LIMIT 10
```

This is a result.
| country |	num |
| - | - |
| CHINA |	574 |
| JAPAN |	347 |
| INDONESIA |	318 |
| IRAN |	254 |
| USA |	217 |
| TURKEY |	207 |
| GREECE |	149 |
| PERU |	148 |
| CHILE |	146 |
| RUSSIA |	138 |

Surprisingly, Japan was not number-1. It was China. But it included weak earthquakes so let's add filter that works more than specific seismic magnitude scales.
Next, let's focus on huge earthquakes. Generally, Magnitude is more than 7 earthquakes are called huge earthquakes.

```sql
SELECT country, COUNT(*) as num, AVG(eq_primary) as avg
FROM `ciccc-lab.final_project.cleaned_earthquakes`
WHERE eq_primary >= 7
GROUP BY country
ORDER BY num DESC
LIMIT 10
```

| country |	num |	avg |
| - | - | - |
| JAPAN |	187 |	7.5374331550802127 |
| INDONESIA |	135 |	7.5762962962962952 |
| CHILE |	97 | 7.6855670103092786 |
| RUSSIA | 96 |	7.6374999999999975 |
| USA |	89 | 7.6460674157303368 |
| CHINA |	89 | 7.4382022471910112 |
| PERU | 84 | 7.7190476190476174 |
| MEXICO |	80 | 7.5474999999999985 |
| PAPUA NEW GUINEA | 66 | 7.5272727272727264 |
| PHILIPPINES |	64 | 7.58125 |

As I expected, Japan has a most number of huge earthquakes.

#### How much damage did they get?

Last section, I finded out 10 countries which has a lot of damage. In this section, I'm going to figure out how much damage they got. this dataset has `total_deaths`, `total_missing`, `total_injuries`, `total_damage_millions_dollars`, `total_houses_destroyed`, and `total_houses_damaged`.

```sql
SELECT
country,
SUM(total_deaths) as total_deaths,
SUM(total_missing) as total_missing,
SUM(total_injuries) as total_injuries,
SUM(total_damage_millions_dollars) as total_damage_millions_dollars,
SUM(total_houses_destroyed) as total_houses_destroyed,
SUM(total_houses_damaged) as total_houses_damaged,
FROM `ciccc-lab.final_project.cleaned_earthquakes`
WHERE country IN
  (SELECT country
  FROM `ciccc-lab.final_project.cleaned_earthquakes`
  WHERE eq_primary >= 7
  GROUP BY country
  LIMIT 10)
GROUP BY country
ORDER BY total_damage_millions_dollars DESC
```

This is a result.
| country |	total_deaths | total_missing | total_injuries |	total_damage_millions_dollars |	total_houses_destroyed | total_houses_damaged |
| - | - | - | - | - | - | - |
| JAPAN |	349725 | 43476 | 142668 |	396394.856 | 1720109 |	414486
| CHINA |	1977993 | 211 | 1319194 |	104575.735 | 9926538 |	21924679
| USA |	1057 | 	| 14992 | 58903.231 |	42155 | 5492 |
| CHILE |	70174  | 31 | 19573 |	35308.591 | 69016 |	529181
| IRAN |	622889 | | 200428 | 10883.4 |	137659 | 67288 |
| NEPAL |	20697 | 366 | 20768 |	10377.5	| 304790 | 269107 |
| INDIA |	60394 | | 201234 | 3263.2 |	378871 | 159451 |
| PERU |	84390 | 138 | 73668 |	816.05 | 83302 |	41356
| FIJI | 7 | | 12 |
| PALAU |

China seems to have a lot of damage more than Japan. But look at `total_damage_millions_dollars`, Japan spent 3.5 times as much money as China. But obviously, Japan and China got a lot of damage more than other country. there is a big gap between top2 and top3.

#### Damage from Tsunami

Last section, I analyzed damage from earthquake. That data included Tsunami damage as well because earthquake can cause Tsunami.
First, Let's figure out how many Tsunami did they have.

```sql
SELECT
country,
COUNT(*) as num_of_earthquake, 
COUNT(CASE WHEN flag_tsunami = "Tsu" THEN 1 END) as num_of_tsunami
FROM `ciccc-lab.final_project.cleaned_earthquakes`
WHERE eq_primary >= 7
GROUP BY country
ORDER BY num_of_tsunami DESC
LIMIT 10
```

This is a result
| country	| num_of_earthquake	| num_of_tsunami |
| - | - | - |
| JAPAN	| 187	| 141 |
| INDONESIA	| 135	| 82 |
| CHILE	| 97	| 74 |
| USA	| 89	| 53 |
| RUSSIA	| 96	| 51 |
| PAPUA NEW GUINEA	| 66	| 43 |
| MEXICO	| 80	| 40 |
| PHILIPPINES	| 64	| 39 |
| PERU	| 84	| 36 |
| SOLOMON ISLANDS	| 47	| 29 |

In Japan, 75% of earthquakes caused Tsunami.

### Conclusion

#### Findings

Most surprise fact is Trukey and Frence weren't in list. As I expected Japn was a top1 country had earthquakes. But damag-ewise, China has gotten really huge damege more than other countries.

#### Recommendation

I strongly recommend that china spend more money on earthquake restoration and prevention. Although Japan didn't have damage as much as China, Japan spend many many money. I think this is why a lot of people died in China because of earthquake.