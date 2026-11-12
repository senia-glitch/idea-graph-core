# Ядро графа идеи

Библиотека без интерфейса и без моделей: карточки, связи, операции, журнал изменений, отмена.

```python
from ideagraph_core import Store, HUMAN, views

store = Store.create("папка-идеи", "Запись к врачу без звонков")
store.apply([{"op": "add_card", "kind": "ветка", "title": "Функции", "parent": "c1"}], HUMAN)
print(views.outline(store))            # оглавление графа — так его читает агент
print(views.changes_text(store, 1))    # что изменилось после ревизии 1
store.undo(store.revision)             # отмена ревизии новой ревизией
```

Правила, которые проверяет ядро: один корень, связи ведут к существующим карточкам, идентификаторы
не повторяются, правка человека главнее правки агента (`base_revision` в `apply`).
Файлы графа лежат в `<папка идеи>/.ideagraph`: `graph.json`, `journal.jsonl`, `layout.json`.

## Установка

```
pip install -e .
```


## Тесты

```
pip install pytest
python -m pytest
```
