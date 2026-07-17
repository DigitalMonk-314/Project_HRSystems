import pytest
from src.db_manager import DatabaseManager


@pytest.fixture
def db():
    db = DatabaseManager()
    db.create_tables()
    return db


def test_create_department(db):
    result = db.add_department("Тестовый отдел")
    result = db.get_all_departments()
    assert len(result) >= 1


def test_create_position(db):
    db.add_department("Отдел разработки")
    db.add_position(1, "Backend разработчик", 250000)
    result = db.get_all_positions()
    assert len(result) >= 1


def test_create_employee(db):
    db.add_department("Отдел тестирования")
    db.add_position(1, "QA инженер", 180000)
    db.add_employee("Иван", 30, 1, 1)
    result = db.get_all_employees()
    assert len(result) >= 1


def test_create_project(db):
    db.add_project("HR System", "Описание проекта")
    result = db.get_all_projects()
    assert len(result) >= 1


def test_employee_project_link(db):
    db.add_department("Отдел безопасности")
    db.add_position(1, "Security Analyst", 300000)
    db.add_employee("Дмитрий", 35, 1, 1)
    db.add_project("Security Audit", "Аудит безопасности")
    db.add_employee_to_project(1, 1)
    result = db.get_employees_in_project(1)
    assert len(result) >= 1
