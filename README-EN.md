# Sprint_1
Learning Python, solving basic tasks.

## task_1
The string contains five time values. They are written separated by commas:
'1h 45m,360s,25m,30m 120s,2h 60s'.  
Write a loop that calculates the total number of minutes. Save the result in a variable and print it on the screen.  
Use the split(), replace() methods and the in operator in your solution.  
Note: a time value can consist of one, two, or three time units.   
Values are decoded as follows:
* hours — any positive integer and the character h;
* minutes — any positive integer and the character m;
* seconds — a positive integer divisible by 60 and the character s.

## task_2
Fix the Tester class so that:
* when calling the work_hard method on the tester_1 class instance, it prints 'tester_1 Можно отдыхать';
* when calling the work_hard method on the tester_2 class instance, it prints 'tester_2 Что ж, ещё часок поработаю!'.

Do not change the function calls.
```
class Tester:
    def __init__(name):
        name = name
        deadline = True

    def work_hard(self, deadline=True):
        if self.deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester(name='tester_1')
tester_1.work_hard(deadline=False)  # 'tester_1 Можно отдыхать'
tester_2 = Tester(name='tester_2')
tester_2.work_hard(deadline=True)   # 'tester_2 Что ж, ещё часок поработаю!' 
```

## task_3
A dictionary contains information about football championships in the 21st century:
* year. For example, 1988;
* the country that won the FIFA World Cup. For example, England.
 
What needs to be done:  
* Add 2022 to the dictionary. In 2022, Argentina became champion.
* Print all champions on the screen in the format year - country.
* Check if Italy won in the 21st century. There is a variable country with the value Italy. Check if it is contained in the dictionary. If yes, print the message Italy became a world football champion in the 21st century!. And if the country is missing from the dictionary values, print Italy did not win the FIFA World Cup in the 21st century.
```
world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}
```

## task_4
There are two task lists. The new_tasks list contains tasks that are planned to be tested by the end of the month. The completed_tasks list contains tasks already completed this month.  
What needs to be done:  
* The tester just completed task_005. Move it from the new_tasks list to the completed_tasks list. Do this in one action.
* The customer removed task_007 from the plan because requirements need to be refined. Delete it from the new_tasks list.
* The customer raised the priority for the last task in the new_tasks list, so it will need to be taken up next. Print it on the screen.
```
new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']
```

## task_5
Write a TestCase class. It should contain a constructor and methods.  
In the constructor, the following fields are initialized:
* steps — test case steps, takes an empty dictionary as a parameter;
* result — the expected result of the test case execution, takes None as a parameter.
 
Methods:
* set_step method — adds a test case step to the steps dictionary. Takes two parameters: step_number and step_text. The key is step_number (step number), and the value is step_text (text description of the step).
* delete_step method — removes a step from steps by the key step_number, which was passed to the method.
* set_result method — sets the expected result. It places it in the result attribute according to the result parameter passed to the method.
* get_test_case method — prints information about the composition of the test case in the format {'Steps': {<step_number>: '<step_description>'}, 'Expected result': '<expected result output>'}.

Example output of the get_test_case method:
```
{
    'Steps': {
            1: 'Перейти на сайт', 
            2: 'Перейти в раздел Товары', 
            3: 'Нажать кнопку «В корзину» у первого товара'
    }, 
    'Expected result': 'Товар окажется в корзине'
} 
class TestCase:

    def __init__(self):
   ...
   ...

test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case() 
```

## task_1_extra
A types dictionary stores bug types. Its keys are numbers from 1 to 5, and values are from 'Blocking' to 'Trivial' respectively. 
```
types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}
```
A tickets dictionary stores tickets (tasks) for these bugs. Keys are severity values from 1 to 5, and values are lists of tickets corresponding to these severity levels. But some tickets have been added multiple times in different lists.
```
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}
```
Compile a summary dictionary where keys are severity levels, such as 'Significant', and values are lists with unique tickets.  
To do this, write two functions: 
* one that removes duplicates from the ticket lists,
* the second that links the severity level to the list of unique tickets.
If a ticket is in one list, it cannot be in lists at a lower severity level.   
The second function takes two parameters: types dictionary with bug types and tickets dictionary with bug lists. The function returns a dictionary where the severity level is linked to the list of unique tickets.  
The final dictionary should look like this:
```
tickets_by_type = {
    'Блокирующий': ['API_45', 'API_76', 'E2E_4'],
    'Критический': ['UI_19', 'API_65', 'E2E_45'],
    'Значительный': ['E2E_2'],
    'Незначительный': ['E2E_9'],
    'Тривиальный': ['API_61']
}
```
Calling the function is optional.

## task_2_extra
Write a function that calculates the digital root of a number.  
To get the digital root of a number, you need to:
* Split the original number into digits by place value.
* Add these digits together.

Do the same with the sum: split it into digits and add them.  
And so on — until you get a single digit (from 1 to 9), which will be the digital root of the number.  
For example, the digital root of 4851 is 9.  
4851 → 4+8+5+1 = 18. 
18 → 1+8 = 9. 
The digital root of 97569 is 9:  
97569 → 9+7+5+6+9 = 36. 
36 → 3+6 = 9. 
A more complex example. For the number 889987, the digital root is 4:  
889987 → 8+8+9+9+8+7 = 49. 
49 → 4+9 = 13. 
13 → 4.

The function can be named digit_root(num). It takes one parameter — num (number), and returns the digital root.
Conditions: 
* the input number is a natural number (1, 2, 3, … );
* the number does not exceed 10**7.
