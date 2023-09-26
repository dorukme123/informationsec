---
## Front matter
lang: ru-RU
title: Информационная безопасность
subtitle: Презентация к лабораторной работе № 4
author:
  - Мерич Дорук Каймакджыоглу.
institute:
  - Российский университет дружбы народов, Москва, Россия
date: 26/09/2023

## i18n babel
babel-lang: russian
babel-otherlangs: english

## Formatting pdf
toc: false
toc-title: Содержание
slide_level: 2
aspectratio: 169
section-titles: true
theme: metropolis
header-includes:
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
---

# Информация

## Докладчик

:::::::::::::: {.columns align=center}
::: {.column width="70%"}

  * Мерич Дорук Каймакджыоглу
  * Студент
  * НКНбд-01-20
  * Российский университет дружбы народов
  * 1032204917
  * <https://github.com/dorukme123>

:::
::: {.column width="30%"}

:::
::::::::::::::

## Актуальность

-Получение практических навыков работы в консоли с расширенными атрибутами файлов.

## Объект и предмет исследования

- Дискреционное разграничение прав в Linux. Расширенные атрибуты.
![1](image/1.png){#fig:000 width=70%}

## Цели и задачи
- От имени пользователя guest определите расширенные атрибуты файла ```/home/guest/dir1/file1``` командой lsattr ```/home/guest/dir1/file1```.
![1](image/1.png){#fig:001 width=70%} 
- Снимите расширенный атрибут a с файла /home/guest/dirl/file1 от имени суперпользователя командой ```chattr -a /home/guest/dir1/file1``` Повторите операции, которые вам ранее не удавалось выполнить. Ваши наблюдения занесите в отчёт. <br>
![2](image/9.png){#fig:002 width=70%}  

## Материалы и методы

- LaTex    
- Процессор **pandoc** для входного формата Markdown    
- Результирующие форматы    
	- **pdf**    
	- **docx**     
- Автоматизация процесса создания: **Makefile**       

## Результаты

в конце мы протестировали наши навыки использования интерфейса командной строки, ознакомились с примерами того, как базовые и расширенные атрибуты используются в управлении доступом.  и протестировал действие на практике расширенных атрибутов "a" и "i".
  

## Итог работы

- Получено **pdf**  из report.md   
- Получено **docx**  из report.md   
- Получено **html** из presentation.md
- Получено **pdf** из presentation.md
- Получено **docx** из presentation.md
- Запись отчета выложен в youtube.com
- Запись презентация выложен в youtube.com
- Запись отчета выложен в rutube.com
- Запись презентация выложен в rutube.com
- Работа выложена в респоситории в github.com
- CHANGELOG.md создано
- Версия на работе создано 