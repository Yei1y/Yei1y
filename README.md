<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img src="assets/banner.svg" alt="叶伟丰 Weifeng Ye — 统计与数据科学" width="100%">
</picture>

经济统计学本科在读（暨南大学经济学院），推免至 **上海财经大学应用统计学**（数据科学与商务统计方向）。

| 加权平均绩点 | 专业排名 | 公开可复现仓库 | 论文 |
| :---: | :---: | :---: | :---: |
| **4.18 / 5.0** | **5 / 85**（前 6%） | **7** 个 | SCI 在投 **1** 篇（审稿返修中） |

> 判断标准只有一条：**结论要能被核验**。脚本编号化、随机种子固定、每一步结果落盘成表，README 里主动写明局限——包括对结论不利的那些。

**作品集（含三维评分表、按岗位裁剪建议）：<https://yei1y.github.io>**

---

## 精选项目

按「含金量 40% + 完成度 30% + 岗位匹配度 30%」加权排序；每一项数字都能在对应仓库的结果文件里查到。

| # | 项目 | 角色 / 性质 | 关键结果 | 仓库 |
| :-: | --- | --- | --- | --- |
| 1 | **企业破产预警「白盒」模型** | 第一完成人 · 全国大学生统计建模大赛广东省三等奖 | 94 项财务指标经杜邦模块样条展开与张量积交叉，显式构造 **31,616 维**交互空间 → 5,218 个候选 → **16 个**非零特征（15 个交互项）；测试集 **AUC 0.9380**、KS 0.7638，91 特征 LightGBM 基线 0.9404（差 0.0024）；漏报 / 误杀成本比 30.5 : 1 下净利润 3,510 / 8,944 万元 | [GitHub](https://github.com/Yei1y/Company-Bankruptcy-Prediction) |
| 2 | **广深两地家用智能健康设备市场调查** | 核心成员（数据模块）· 市场调查与分析大赛省级一等奖 + 省级大创 | 企业委托、全部数据自采：广深 2 城 21 街道 **747 + 444** 份有效问卷、841 + 476 分钟访谈、4,000 条电商评论；加权 K-Means 三类人群 13.19% / 56.35% / 30.46%；SEM 解释方差 **68.7%**（RMSEA 0.030，α = 0.983） | 委托项目，底稿涉密 |
| 3 | **GCor-SIS：超高维生存数据的稳健特征筛选**<br>`论文项目` | 第二作者（第一作者：导师姜云卢教授）· SCI 期刊 *Communications in Statistics – Simulation and Computation* 审稿返修中 · 2026-05 于中国人民大学第二届全国高校本科生统计论坛作报告 | 基于格罗滕迪克相关的**无模型**筛选 + 数据拆分反射控制 FDR ≤ α + o(1)；强筛选一致性的证明**无需次指数尾部条件**；NKI295 乳腺癌数据 **C-index 0.7603**（对比方法中最高），识别出 QSOX2、NUSAP1 等已验证预后基因 | 论文审稿中，代码暂不公开 |
| 4 | **北京住房价格：特征价格模型与多元回归实证** | 独立完成 · 现代回归分析课程论文 | **318,160 条**链家成交记录、64 个特征；半对数 + 时间×区域双向固定效应；近地铁溢价被朴素对比高估约 **4.8 倍**（27.6% → 5.8%）；R² 0.8185，更精确的多项式模型因条件数 1.11 × 10¹² 被否 | [GitHub](https://github.com/Yei1y/beijing-housing-regression) |
| 5 | **AI 采纳与生产率：双重机器学习因果推断** | 独立完成 · 自主研究工作论文（含完整 LaTeX 论文与可复现代码） | **15 万家企业** × 43 字段 → 64 维前定协变量；手写 Neyman 正交评分 + 5 折交叉拟合，不调用高层 API；ATE = **+0.6%（p = 0.342，不显著）**，LASSO / RF / XGBoost 三法一致；因果森林显示 CATE 标准差 0.044（≈ ATE 的 8 倍） | [GitHub](https://github.com/Yei1y/ai-adoption-productivity-dml) |
| 6 | **电商用户行为漏斗分析与转化建模**<br>`电商项目` | 独立完成 · 公开项目的批判式复现与深挖 | MySQL 8.0 显式 DDL + **24 条查询**（窗口函数算占比）；定位「详情页 → 支付页」段转化率仅 **12.63%**（流失 41,870 次）；卡方 + **BH 校正** + Cramér's V 判定 8 个维度中仅活跃度有实质关联（V = 0.2657） | [GitHub](https://github.com/Yei1y/user-behavior-funnel-analysis) |

另有 2 个项目（中文新闻分类 LSTM vs 朴素贝叶斯、影评情感分析四模型对比）侧重实验对照与数据质量核查——两者都识别出了原本看起来成立的结论里的隐患。见[项目全集](https://yei1y.github.io/projects/)。

---

## 两张图

**图 1 · 电商漏斗：10 万条会话里唯一该优先动的环节**
`详情页 → 支付页` 段转化率只有 12.63%，流失 41,870 次，约为第二大流失点的 10 倍；前两段仍维持在 67%–74%。

<img src="assets/fig-funnel.png" width="880" alt="电商用户行为漏斗：首页 97,274 → 列表页 71,684（↓73.69%）→ 详情页 47,922（↓66.85%）→ 支付页 6,052（↓12.63%）→ 确认页 1,684（↓27.83%）">

**图 2 · 因果推断：换掉 nuisance 估计量与交叉拟合折数，结论仍是零**
五种设定的 95% 置信区间全部覆盖 0（ATE ∈ [0.0004, 0.0059]）。这个项目交付的不是一个效应估计，而是一个**可辩护的零**——把「没有效应」写成结论，和把效应写显著需要同等证据。

<img src="assets/fig-ate.png" width="880" alt="ATE 森林图：随机森林 5 折 +0.59%（p=0.342）、LASSO +0.04%、XGBoost +0.42%、K=10 +0.51%、K=2 +0.58%，95% 置信区间均覆盖 0">

两张图都由 [tools/make_figures.py](tools/make_figures.py) 从仓库结果文件生成，不手抄数值。

---

## 按岗位看同一批项目

同一批工作，投不同岗位时我会换一套讲法与顺序：

| 目标岗位 | 先讲哪个 | 讲什么 | 哪些压成一行 |
| --- | --- | --- | --- |
| **数据分析 / 商业分析** | 市场调查 → 电商漏斗 → 破产预警 | 「业务问题 → 口径 → 结论 → 建议」的闭环，SQL 取数与漏斗归因 | GCor-SIS 只作为方法学背书 |
| **数据科学 / 算法工程** | 破产预警 → GCor-SIS → DML | 高维、稀疏、类别不平衡、可复现；Rcpp 并行与内存控制 | 市场调查只说明业务侧也能承接 |
| **AI 产品运营 / 增长** | 市场调查 → 电商漏斗 | 用户洞察到可执行策略的完整链条 | 方法论细节全部淡化 |
| **研究岗 / 升学申请** | GCor-SIS → DML → 破产预警 | 引理证明、蒙特卡洛设计、从零实现估计量 | 课程论文只列题目 |

---

## 能力

| 维度 | 体现 |
| --- | --- |
| **统计方法** | 特征筛选（SIS / SCAD）、惩罚回归、生存分析、因果推断（DML / 因果森林 / CATE）、回归诊断、抽样设计、列联表与效应量、多重比较校正（BH）、聚类、SEM |
| **编程** | R（Rcpp C++ 扩展、20 核并行、内存峰值控制）· Python（pandas / statsmodels / scikit-learn / PyTorch / EconML）· SQL（MySQL 8.0，显式 DDL 与窗口函数）· LaTeX · SPSS / AMOS |
| **工程与可复现** | 脚本编号化且自包含、随机种子固定、结果落盘 CSV、代码与结论分离、Git / GitHub |
| **诚实标注的空白** | 尚无实习经历；Docker / 服务部署、API 与 RAG / Agent 工作流、A/B 实验设计与 SQL 留存取数尚未实操——这些都不在技能栏里，正在补。 |

---

## 数字怎么核验

每个数都能顺着这条路径查回去，不必相信我：

| 数字 | 去哪查 |
| --- | --- |
| 六维评分与排序 | [项目全集](https://yei1y.github.io/projects/) 的三线表，评分口径写在表注 |
| 破产预警 AUC 0.9380 | `Company-Bankruptcy-Prediction/results/tables/model_metrics_scad.csv`，或由 `test_probabilities.csv` 重算 |
| 净利润 3,510 / 8,944 万元 | `Company-Bankruptcy-Prediction/results/tables/economic_scenarios.csv` |
| 16 个非零特征 | `Company-Bankruptcy-Prediction/results/tables/scad_selected_features.csv` |
| 电商漏斗 12.63% | `user-behavior-funnel-analysis` 的 SQL 输出表与 `results.md` |
| DML 的 ATE 与稳健性 | `ai-adoption-productivity-dml/output/tables/dml_results.csv` 与 `robustness_results.csv` |
| 房产回归系数与诊断 | `beijing-housing-regression/output/tables/vif_results.csv`、`consensus_ols_coefficients.csv` |

---

## 荣誉（部分）

2025 **国家奖学金** · 第十六届全国大学生数学竞赛广东省**一等奖** · 全国大学生市场调查与分析大赛广东赛区**省级一等奖** · 全国大学生统计建模大赛广东省三等奖 · MathorCup 数学应用挑战赛国家级三等奖 · 全国计算机等级考试二级（MySQL，良好）· CET-6 551

---

## 联系

**邮箱** yeily_github@163.com &nbsp;·&nbsp; **作品集** <https://yei1y.github.io> &nbsp;·&nbsp; **现居** 广州（就学）

正在寻找 **数据科学 / 数据分析**方向的实习机会（AI 产品与增长相关岗位同样欢迎）：广州优先，深圳可接受。
