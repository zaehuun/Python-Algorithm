-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, 
CASE WHEN SEX_UPON_INTAKE LIKE "Neutered%" or SEX_UPON_INTAKE LIKE "Spayed%" THEN "O"
     ELSE "X"
     END
FROM ANIMAL_INS;
