Probably-the-most-miserable-attempt-to-create-chess
===================================================

Шах
Целта на играта е да се матира противника. Играта ще е за двама човека, играещи на една машина.

Класове за всяка фигура, всеки съдържащ:
-Име на фигурата
-Цвят на фигурата
-Текуща позиция
-Предишна позиция
-Индикатор дали фигурата е била местена(главно заради царя и топа)
-Проверка дали ход е валиден - гледа се дали е подаден валиден адрес(дали е в дъската), дали квадтачето е свободно или заето от чужда фигура, дали квадратчето е достъпно за дадената фигура. Проверката дали царя не отива на бито поле и проверката за рокада се извършват от класа за игра

Клас за квадратче от дъската:
-Адрес(примерно B4, D2…)
-Фигура в квадратчето(None, ако е свободно)

Клас за дъска:
-Двумерен масив от квадратчета
-Индексация, посредством адресите на квадратчетата
-Функция за показване на дъската

Клас за игра:
-Списък от белите фигури
-Списък от черните фигури
-Функция за създаване на игра – инициализиране на дъската и фигурите на началните им позции
-Играч на ход
-Ход на играча
-Функция за проверка дали ход е валиден
-Проверка за шах, пат и мат
-Брояч на ходовете

Планове до Milestone II:
Класовете за фигурите, класа за квадратче и класа за дъска
