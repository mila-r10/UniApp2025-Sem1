from student import Student
from subject import Subject
from database import Database

def print_header(title: str):
    print(f"\n=== {title} ===")


def main():
    # 使用测试用数据库文件，避免覆盖正式数据
    db = Database(path='test_students.data')

    # 清空数据库
    print_header('清空数据库')
    db.clear_all()
    print('数据库已清空。')

    # 添加学生
    print_header('添加新学生')
    s1 = Student(name='张三', email='zhangsan@university.com', password='Abcde123')
    db.add_student(s1)
    print(f"添加学生: ID={s1.id}, 姓名={s1.name}, 邮箱={s1.email}")

    s2 = Student(name='李四', email='lisi@university.com', password='Qwert123')
    db.add_student(s2)
    print(f"添加学生: ID={s2.id}, 姓名={s2.name}, 邮箱={s2.email}")



    # 列出所有学生
    print_header('列出所有学生')
    for stu in db.list_all():
        avg = stu.average_mark()
        status = '通过' if stu.passed() else '不通过'
        print(f"ID={stu.id}, 姓名={stu.name}, 平均分={avg:.2f}, 状态={status}")



    # 根据邮箱获取学生
    print_header('根据邮箱获取学生')
    stu = db.get_student_by_email('zhangsan@university.com')
    print(f"找到了学生: {stu.name} (ID={stu.id})")

    # 添加一门新科目
    subject = stu.enroll()
    print(f"添加成功: 科目ID={123}，分数={321}，等级={subject.grade}")

    print("当前学生所选科目如下：")
    for sub in stu.subjects:
        print(f"科目ID={sub.id}，分数={sub.mark}，等级={sub.grade}")


    # 修改密码并更新
    print_header('修改密码')
    stu.change_password('Xyzabc123')
    db.update_student(stu)
    print(f"密码已更新为: {stu.password}")



    # 退选一个科目
    print_header('退选科目')
    if stu.subjects:
        sub_id = stu.subjects[0].id
        stu.remove_subject(sub_id)
        db.update_student(stu)
        print(f"已移除科目ID={sub_id}")
    else:
        print('未找到科目可移除。')



    # 分区学生 - pass 还是 fail
    print_header('分区学生（PASS/FAIL）')
    parts = db.partition_students()
    print('通过的学生:', [s.name for s in parts['pass']])
    print('未通过的学生:', [s.name for s in parts['fail']])



    # 按 WAM 分组
    print_header('按平均分分组')
    groups = db.group_students_by_grade()
    for avg, studs in groups.items():
        print(f"平均分 {avg}: {[s.name for s in studs]}")



    # 删除学生
    print_header('删除学生')
    db.remove_student_by_id(s2.id)
    print(f"已删除学生ID={s2.id}")
    print('当前学生列表:', [s.name for s in db.list_all()])



   # 清空数据库
    print_header('清空数据库')
    db.clear_all()
    print('数据库已清空。')

if __name__ == '__main__':
    main()