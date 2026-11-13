# Ядро графа идеи

Библиотека без интерфейса и без моделей: карточки, связи, операции, журнал изменений, отмена.

```python
from idea_graph_core import Store, HUMAN, views

store = Store.create("папка-проекта", "Запись к врачу")       # пустой граф: корневой карточки нет
store.apply([{"op": "add_card", "kind": "домен", "title": "Пациенты частных клиник"}], HUMAN)
store.apply([{"op": "add_card", "kind": "сценарий", "title": "Утром нужно записаться", "parent": "c1"}], HUMAN)
print(views.outline(store))            # оглавление графа — так его читает агент
print(views.changes_text(store, 1))    # что изменилось после ревизии 1
store.undo(store.revision)             # отмена ревизии новой ревизией
```

Правила, которые проверяет ядро: связи ведут к существующим карточкам, идентификаторы
не повторяются, правка человека главнее правки агента (`base_revision` в `apply`).
Файлы графа лежат в `<папка проекта>/.idea-graph`: `graph.json`, `journal.jsonl`, `layout.json`.

## Установка

```
pip install -e .
```


## Тесты

```
pip install pytest
python -m pytest
```
