from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/publications')
def publications():
    return render_template('publications.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/team')
def team():
    # 获取团队成员数据
    members = get_team_members()
    
    # 按年级分组
    first_year = [members[i] for i in range(2, 8)]  # 6个一年级研究生
    second_year = [members[i] for i in range(9, 15)]  # 6个二年级研究生
    third_year = [members[i] for i in range(15, 21)]  # 6个三年级研究生
    
    # 团队负责人
    team_lead = members[1]
    
    return render_template('team.html', 
                          team_lead=team_lead,
                          first_year=first_year,
                          second_year=second_year,
                          third_year=third_year)

def get_team_members():
    # 团队成员数据
    members = {
        1: {
            "name": "董玉民",
            "name_en": "Dong Yumin",
            "title": "团队负责人，教授",
            "email": "dongyumin@cqnu.edu.cn",
            "photo": "cqnu_gate.jpg",
            "bio": "董玉民是重庆师范大学计算机与信息科学学院的教授。他的研究兴趣包括量子计算、量子信息、人工智能、并行计算以及ERP等。",
            "education": [
                {"year": "2007", "degree": "控制理论与控制工程博士学位", "institution": "华东理工大学，中国"},
                {"year": "1997", "degree": "计算机应用硕士学位", "institution": "东北大学，中国"},
                {"year": "1988", "degree": "无线电专业学士学位", "institution": "辽宁大学，中国"}
            ],
            "research_interests": ["量子计算", "量子信息", "量子机器学习", "大模型", "智能体", "量子图像处理", "量子随机行走", "量子聚类"],
            "publications": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "projects": [1, 2, 3, 4, 5]
        },
    }
    
    # 添加7个一年级硕士研究生
    first_year_names = ["查新纪", "陈群", "宋学亮", "江启浩", "杨渝楠", "蔡屿璐"]
    first_year_names_en = ["Zha Xinji", "Chen Qun", "Song Xueliang", "Jiang Qihao", "Yang Yunan", "Cai Yulu"]
    
    for i, (name, name_en) in enumerate(zip(first_year_names, first_year_names_en), 2):
        members[i] = {
            "name": name,
            "name_en": name_en,
            "title": "硕士研究生（一年级）",
            "email": f"{name_en.lower().replace(' ', '')}@cqnu.edu.cn",
            "photo": "cqnu_gate.jpg",
            "bio": f"{name}是重庆师范大学计算机与信息科学学院的一年级硕士研究生。研究方向为量子计算与量子信息处理。",
            "education": [
                {"year": "2023", "degree": "计算机科学学士学位", "institution": "重庆师范大学计算机与信息科学学院"}
            ],
            "research_interests": ["量子计算", "量子信息", "量子机器学习", "大模型", "智能体", "量子图像处理", "量子随机行走", "量子聚类"][i % 7:] + ["量子计算", "量子信息", "量子机器学习", "大模型", "智能体", "量子图像处理", "量子随机行走", "量子聚类"][:(i % 7)],
            "publications": [],
            "projects": [i % 5 + 1]
        }
    
    # 添加6个二年级硕士研究生
    second_year_names = ["吴高杰", "刘丽诗", "丁焕欣", "吴双", "孙同磊", "倪啸峰"]
    second_year_names_en = ["Wu Gaojie", "Liu Lishi", "Ding Huanxin", "Wu Shuang", "Sun Tonglei", "Ni Xiaofeng"]
    
    for i, (name, name_en) in enumerate(zip(second_year_names, second_year_names_en), 9):
        members[i] = {
            "name": name,
            "name_en": name_en,
            "title": "硕士研究生（二年级）",
            "email": f"{name_en.lower().replace(' ', '')}@cqnu.edu.cn",
            "photo": "cqnu_gate.jpg",
            "bio": f"{name}是重庆师范大学计算机与信息科学学院的二年级硕士研究生。研究方向为量子计算与量子信息处理。",
            "education": [
                {"year": "2022", "degree": "计算机科学学士学位", "institution": "重庆师范大学计算机与信息科学学院"}
            ],
            "research_interests": ["量子计算", "量子信息", "量子机器学习", "大模型", "智能体", "量子图像处理", "量子随机行走", "量子聚类"][i % 7:] + ["量子计算", "量子信息", "量子机器学习", "大模型", "智能体", "量子图像处理", "量子随机行走", "量子聚类"][:(i % 7)],
            "publications": [i % 3 + 1] if i > 10 else [],
            "projects": [i % 5 + 1]
        }
    
    # 添加6个三年级硕士研究生
    third_year_names = ["颜瑞", "牟定康", "李菲菲", "朱婷婷", "尹深昊", "徐宸"]
    third_year_names_en = ["Yan Rui", "Mou Dingkang", "Li Feifei", "Zhu Tingting", "Yin Shenhao", "Xu Chen"]
    
    for i, (name, name_en) in enumerate(zip(third_year_names, third_year_names_en), 15):
        members[i] = {
            "name": name,
            "name_en": name_en,
            "title": "硕士研究生（三年级）",
            "email": f"{name_en.lower().replace(' ', '')}@cqnu.edu.cn",
            "photo": "cqnu_gate.jpg",
            "bio": f"{name}是重庆师范大学计算机与信息科学学院的三年级硕士研究生。研究方向为量子计算与量子信息处理。",
            "education": [
                {"year": "2021", "degree": "计算机科学学士学位", "institution": "重庆师范大学计算机与信息科学学院"}
            ],
            "research_interests": ["量子计算", "量子信息", "量子机器学习", "大模型", "智能体", "量子图像处理", "量子随机行走", "量子聚类"][i % 7:] + ["量子计算", "量子信息", "量子机器学习", "大模型", "智能体", "量子图像处理", "量子随机行走", "量子聚类"][:(i % 7)],
            "publications": [i % 5 + 1],
            "projects": [i % 5 + 1]
        }
    
    return members

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/member/<int:member_id>')
def member_detail(member_id):
    # 获取团队成员数据
    members = get_team_members()
    member = members.get(member_id, members[1])  # 默认返回第一个成员
    return render_template('member_detail.html', member=member)

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/publication/<int:pub_id>')
def publication_detail(pub_id):
    # 这里可以根据pub_id获取特定论文的详细信息
    # 为简化示例，我们使用固定数据
    publications = {
        1: {
            "title": "基于分数阶理论的量子反向传播神经网络",
            "authors": "董玉民, 张津磊, 肖淑芬",
            "journal": "数学的方法与应用科学, 2021, 44(18): 14016-14028",
            "year": 2021,
            "abstract": "本研究探讨了分数阶理论在量子反向传播神经网络中的应用。我们提出了一种新型的分数阶量子神经网络模型，能够有效处理量子信息并提高网络的学习能力。实验结果表明，与传统量子神经网络相比，我们的分数阶模型在某些特定任务上展现出显著的性能优势。",
            "keywords": ["分数阶理论", "量子神经网络", "量子计算", "机器学习", "量子信息处理"],
            "doi": "https://doi.org/10.1002/mma.7442",
            "pdf_link": "#",
            "related_publications": [2, 3, 8]
        },
        2: {
            "title": "求解非线性方程的改进混合量子优化算法",
            "authors": "董玉民, 张津磊, 肖淑芬",
            "journal": "量子信息处理, 2021, 20(7): 202",
            "year": 2021,
            "abstract": "本研究提出了一种改进的混合量子优化算法，用于求解非线性方程。我们通过引入新型量子参数化电路和优化策略，显著提高了算法在处理复杂非线性方程时的性能。实验结果表明，我们的方法在求解精度和收敛速度方面具有明显优势。",
            "keywords": ["量子优化", "非线性方程", "量子计算", "混合量子算法", "量子电路"],
            "doi": "https://doi.org/10.1007/s11128-021-03139-4",
            "pdf_link": "#",
            "code_link": "#",
            "related_publications": [1, 3, 9]
        },
        3: {
            "title": "基于Caputo型分数阶量子神经网络的稳定性分析",
            "authors": "董玉民, 肖淑芬, 张津磊",
            "journal": "函数空间杂志, 2021, 文章ID 5558818",
            "year": 2021,
            "abstract": "本文研究了基于Caputo型分数阶量子神经网络的稳定性分析。我们提出了一种新型的分数阶量子神经网络模型，并对其稳定性进行了理论分析和数值验证。研究结果表明，该模型在处理量子信息时具有良好的稳定性和鲁棒性，为量子神经网络的实际应用提供了理论基础。",
            "keywords": ["分数阶微积分", "量子神经网络", "稳定性分析", "Caputo型分数阶导数", "量子计算"],
            "pdf_link": "#",
            "related_publications": [1, 2, 4, 8]
        },
        4: {
            "title": "正则图中特殊顶点的量子搜索算法及其电路实现",
            "authors": "董玉民, 张津磊, 肖淑芬",
            "journal": "国际理论物理杂志, 2021, 60(9): 3023-3035",
            "year": 2021,
            "abstract": "本文探讨了量子搜索算法在正则图中寻找特殊顶点的应用。我们提出了一种基于量子行走的搜索算法，能够有效识别正则图中的特殊顶点，并设计了相应的量子电路实现。通过与经典算法的比较，我们展示了量子方法在特定图结构上的计算优势。",
            "keywords": ["量子搜索算法", "正则图", "量子电路", "量子行走", "量子计算"],
            "pdf_link": "#",
            "code_link": "#",
            "related_publications": [3, 5, 9]
        },
        5: {
            "title": "基于量子图像分解的量子图像加密",
            "authors": "董玉民, 肖淑芬, 张津磊",
            "journal": "国际理论物理杂志, 2021, 60(7): 2501-2516",
            "year": 2021,
            "abstract": "本研究提出了一种基于量子图像分解的量子图像加密方法。我们的方法利用量子图像分解技术，实现了高效的量子图像加密和解密。理论分析和数值模拟表明，该方法具有高安全性和计算效率，为量子图像处理和量子密码学提供了新的技术路径。",
            "keywords": ["量子图像处理", "量子加密", "量子图像分解", "量子信息", "量子密码学"],
            "pdf_link": "#",
            "related_publications": [3, 4, 8]
        },
        6: {
            "title": "基于改进量子优化算法的支持向量机天气预测技术",
            "authors": "董玉民, 张津磊, 肖淑芬",
            "journal": "计算智能与神经科学, 2021, 文章ID 5558818",
            "year": 2021,
            "abstract": "本研究探讨了改进量子优化算法在支持向量机天气预测中的应用。我们提出了一种新型的量子优化支持向量机模型，显著提高了天气预测的准确性和效率。实验结果表明，我们的方法在多个天气预测任务上取得了优异的性能，并在计算效率方面展现出量子计算的潜力。",
            "keywords": ["量子优化算法", "支持向量机", "天气预测", "量子计算", "机器学习"],
            "doi": "https://doi.org/10.1155/2021/5558818",
            "pdf_link": "#",
            "code_link": "#",
            "related_publications": [2, 7, 9]
        },
        7: {
            "title": "量子甲虫群算法优化的极限学习机入侵检测",
            "authors": "董玉民, 肖淑芬, 张津磊",
            "journal": "量子信息处理, 2022, 21(3): 85",
            "year": 2022,
            "abstract": "本研究提出了一种基于量子甲虫群算法优化的极限学习机入侵检测方法，能够在复杂网络环境中实现高效的安全监测。我们设计了一种新型的量子优化框架和自适应学习网络，显著提高了入侵检测的准确性和效率。实验结果表明，我们的方法在多个入侵检测基准数据集上取得了优异的性能。",
            "keywords": ["量子甲虫群算法", "极限学习机", "入侵检测", "量子优化", "网络安全"],
            "doi": "https://doi.org/10.1007/s11128-022-03438-4",
            "pdf_link": "#",
            "code_link": "#",
            "related_publications": [6, 9]
        },
        8: {
            "title": "基于量子计算的分数阶神经网络及其在图像处理中的应用",
            "authors": "董玉民, 张津磊, 肖淑芬, 李明",
            "journal": "量子信息与计算, 2023, 23(5-6): 401-420",
            "year": 2023,
            "abstract": "本研究提出了一种基于量子计算的分数阶神经网络模型，并探讨了其在图像处理领域的应用。我们结合量子计算和分数阶微积分的优势，设计了一种新型神经网络结构，能够有效处理复杂图像信息。实验结果表明，该模型在图像去噪、分割和识别等任务上表现出色，为量子计算在图像处理领域的应用提供了新的思路。",
            "keywords": ["量子计算", "分数阶神经网络", "图像处理", "量子机器学习", "分数阶微积分"],
            "doi": "https://doi.org/10.26421/QIC23.5-6-1",
            "pdf_link": "#",
            "code_link": "#",
            "related_publications": [1, 3, 5]
        },
        9: {
            "title": "量子近似优化算法在组合优化问题中的应用研究",
            "authors": "董玉民, 肖淑芬, 张津磊, 王强",
            "journal": "物理评论A, 2023, 107(4): 042413",
            "year": 2023,
            "abstract": "本研究探讨了量子近似优化算法(QAOA)在解决组合优化问题中的应用。我们提出了一种改进的QAOA变体，通过优化参数策略和电路结构，显著提高了算法在处理大规模组合优化问题时的性能。实验结果表明，我们的方法在最大割问题、旅行商问题等典型组合优化问题上取得了优异的结果，展示了量子计算在优化领域的潜力。",
            "keywords": ["量子近似优化算法", "组合优化", "量子计算", "量子电路", "最大割问题"],
            "doi": "https://doi.org/10.1103/PhysRevA.107.042413",
            "pdf_link": "#",
            "code_link": "#",
            "related_publications": [2, 4, 6, 7]
        }
    }
    
    pub = publications.get(pub_id, publications[1])  # 默认返回第一篇论文
    return render_template('publication_detail.html', publication=pub)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    # 这里可以根据project_id获取特定项目的详细信息
    # 为简化示例，我们使用固定数据
    projects = {
        1: {
            "title": "基于量子随机游走的分布并行智能处理的理论和方法",
            "period": "2018 - 2021",
            "funding": "国家自然科学基金面上项目 (61772295)",
            "description": "该项目旨在研究基于量子随机游走的分布并行智能处理理论和方法，探索量子计算在分布式系统中的应用潜力。我们专注于设计基于量子随机游走的并行算法，并研究其在大规模数据处理、优化问题求解和模式识别等领域的实际应用。",
            "research_directions": ["量子随机游走理论", "分布式量子算法", "量子并行计算", "量子优化", "量子模式识别"],
            "partners": ["重庆师范大学", "青岛理工大学", "华东理工大学"],
            "achievements": [
                "提出了新型量子随机游走模型",
                "开发了基于量子随机游走的分布式算法框架",
                "在大规模数据处理中实现了量子加速",
                "发表了多篇高水平学术论文"
            ],
            "gallery_images": ["cqnu_gate.jpg", "cqnu_gate.jpg", "cqnu_gate.jpg"],
            "related_publications": [1, 3, 4],
            "team_members": list(range(1, 8))  # 团队成员1-7
        },
        2: {
            "title": "基于量子随机行走智能处理的理论和方法",
            "period": "2016 - 2016",
            "funding": "国家自然科学基金面上项目 (61572270)",
            "description": "该研究方向专注于量子随机行走在智能处理中的理论和方法研究，以提高计算效率和处理能力。我们研究量子随机行走在图结构上的行为特性，并探索其在搜索、优化和机器学习等领域的应用。",
            "research_content": ["量子随机行走模型", "量子搜索算法", "量子优化方法", "量子机器学习", "量子信息处理"],
            "application_areas": ["组合优化", "图数据分析", "模式识别", "量子通信"],
            "achievements": [
                "建立了量子随机行走的理论框架",
                "开发了基于量子随机行走的搜索算法",
                "实现了量子优化方法在组合问题中的应用",
                "发表了多篇高水平学术论文"
            ],
            "gallery_images": ["cqnu_gate.jpg", "cqnu_gate.jpg"],
            "related_publications": [2, 5],
            "team_members": list(range(6, 13))  # 团队成员6-12
        },
        3: {
            "title": "基于量子聚类的MAS群体智能处理的理论和方法",
            "period": "2012 - 2015",
            "funding": "国家自然科学基金面上项目 (61173056)",
            "description": "该项目致力于研究基于量子聚类的多智能体系统(MAS)群体智能处理理论和方法，包括量子聚类算法、多智能体协作机制和群体智能优化等。我们开发基于量子计算的聚类方法，为多智能体系统提供高效的协作决策支持。",
            "research_content": ["量子聚类算法", "多智能体系统", "群体智能优化", "量子协作决策"],
            "achievements": [
                "提出了量子聚类的理论模型",
                "开发了基于量子计算的多智能体协作框架",
                "实现了群体智能在复杂问题中的应用",
                "发表了多篇高水平学术论文"
            ],
            "gallery_images": ["cqnu_gate.jpg", "cqnu_gate.jpg"],
            "code_link": "#",
            "related_publications": [3, 4, 5],
            "team_members": list(range(10, 17))  # 团队成员10-16
        },
        4: {
            "title": "基于量子计算的人工智能天气预测",
            "period": "2020 - 2023",
            "funding": "重庆市教委科学技术研究计划项目 (KJZD-M202000501)",
            "description": "该项目研究基于量子计算的人工智能天气预测技术，探索量子优化算法在气象数据处理和天气预测中的应用。我们致力于开发高精度、高效率的量子天气预测模型，为气象预报提供新的技术路径。",
            "research_content": ["量子优化算法", "气象数据处理", "天气预测模型", "量子机器学习"],
            "achievements": [
                "开发了基于量子优化的支持向量机天气预测方法",
                "提出了量子气象数据处理框架",
                "设计了量子-经典混合天气预测系统",
                "发表了多篇高水平学术论文"
            ],
            "gallery_images": ["cqnu_gate.jpg"],
            "code_link": "#",
            "related_publications": [2, 6],
            "team_members": list(range(15, 20)) + [1]  # 团队成员15-19和1
        },
        5: {
            "title": "高场强MRI的量子方法在脑出血转化的研究",
            "period": "2023 - 至今",
            "funding": "重庆市自然科学基金重点项目 (CSTB2023NSCQ-LZX0139)",
            "description": "该项目致力于研究高场强MRI的量子方法在脑出血转化中的应用，探索量子计算在医学图像处理和疾病诊断中的新方法。我们专注于开发基于量子计算的MRI图像处理算法、量子特征提取和量子辅助诊断技术，推动量子计算在医学领域的应用。",
            "research_directions": ["量子图像处理", "量子特征提取", "量子辅助诊断", "医学图像分析", "脑出血转化机制"],
            "partners": ["重庆师范大学", "重庆医科大学", "重庆市人民医院"],
            "achievements": [
                "开发了基于量子计算的MRI图像处理方法",
                "提出了量子特征提取算法",
                "在脑出血转化研究中取得初步成果",
                "发表了相关学术论文"
            ],
            "gallery_images": ["cqnu_gate.jpg", "cqnu_gate.jpg"],
            "code_link": "#",
            "related_publications": [4, 7],
            "team_members": list(range(5, 15)) + [1]  # 团队成员5-14和1
        }
    }
    
    project = projects.get(project_id, projects[1])  # 默认返回第一个项目
    return render_template('project_detail.html', project=project)

@app.route('/google-scholar')
def google_scholar():
    # 重定向到Google Scholar页面
    return redirect("https://scholar.google.com/")

@app.route('/github')
def github():
    # 重定向到GitHub页面
    return redirect("https://github.com/")

@app.route('/linkedin')
def linkedin():
    # 重定向到LinkedIn页面
    return redirect("https://www.linkedin.com/")

@app.route('/email')
def email():
    # 重定向到邮件客户端
    return redirect("mailto:dongyumin@cqnu.edu.cn")

@app.route('/news')
def news():
    # 新闻动态页面
    return render_template('news.html')

@app.route('/contact')
def contact():
    # 联系我们页面
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True) 