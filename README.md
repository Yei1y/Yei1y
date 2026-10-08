<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img src="assets/banner.svg" alt="叶伟丰 Weifeng Ye - Statistics, Causal Inference, Machine Learning" width="100%">
</picture>

<p align="center">
  经济统计学 | 暨南大学 &nbsp;&middot;&nbsp; 推免至上海财经大学应用统计学（数据科学与商务统计）<br>
  用统计建模、因果推断与机器学习，把复杂数据变成可验证的判断。
</p>

<p align="center">
  <a href="#代表项目">项目</a> &nbsp;&middot;&nbsp;
  <a href="#方法与工具">方法与工具</a> &nbsp;&middot;&nbsp;
  <a href="https://yei1y.github.io">完整作品集</a> &nbsp;&middot;&nbsp;
  <a href="mailto:yeily_github@163.com">联系我</a>
</p>

---

## 代表项目

| 项目 | 我解决的问题 | 结果与方法 |
| --- | --- | --- |
| **[企业破产预警：可解释的白盒模型](https://github.com/Yei1y/Company-Bankruptcy-Prediction)** | 在高维财务信息中识别真正有决策价值的风险信号 | 将 94 项指标展开为 31,616 维交互空间，筛至 **16 个**可解释特征；测试集 **AUC 0.9380**、KS 0.7638。以代价敏感决策连接模型评分与信贷利润。 |
| **[AI 采纳与生产率：双重机器学习](https://github.com/Yei1y/ai-adoption-productivity-dml)** | 控制高维混杂后，AI 采纳是否带来生产率提升 | 在 **150,000** 家企业、64 个前定协变量上手写 Neyman 正交评分与交叉拟合；ATE = **+0.59%**，p = 0.342。不同 nuisance 模型下结论稳定为不显著。 |
| **[北京住房价格：特征价格模型](https://github.com/Yei1y/beijing-housing-regression)** | 区分地铁可达性与区位条件对房价的影响 | 分析 **318,160** 条成交记录；近地铁的朴素溢价为 27.6%，控制时间与区域效应后为 **5.8%**，避免把区位效应误判为交通效应。 |
| **[电商用户行为漏斗分析](https://github.com/Yei1y/user-behavior-funnel-analysis)** | 找到应优先优化的转化环节，并检验用户差异是否有业务意义 | 使用 MySQL 8.0 构建漏斗与统计检验流程；详情页到支付页转化仅 **12.63%**，流失 **41,870** 次会话。 |

<p align="right"><a href="https://yei1y.github.io/projects/">查看全部项目与研究产出 -&gt;</a></p>

## 从结果开始

<details open>
<summary><strong>电商转化：定位唯一需要优先处理的瓶颈</strong></summary>
<br>
<img src="assets/fig-funnel.png" width="880" alt="电商漏斗显示详情页到支付页的转化率仅为 12.63%，是最大的流失环节。">
</details>

<details>
<summary><strong>因果推断：稳健性设定下的零效应结论</strong></summary>
<br>
<img src="assets/fig-ate.png" width="880" alt="不同估计器和交叉拟合折数下，AI 采纳的平均处理效应置信区间均覆盖零。">
</details>

图表由项目结果文件生成；它们展示的不只是模型输出，也展示结果在不同设定下是否站得住。

## 方法与工具

| 工作环节 | 常用工具 | 代表方法 |
| --- | --- | --- |
| 数据处理与分析 | Python, pandas, NumPy, SQL / MySQL | 数据质量核查、特征工程、漏斗分析、统计推断 |
| 建模与评估 | scikit-learn, statsmodels, R | 回归诊断、稀疏建模、集成学习、交叉验证、代价敏感决策 |
| 统计研究 | R, Rcpp, LaTeX | 因果推断、双重机器学习、生存分析、高维特征筛选、蒙特卡洛模拟 |
| 交付与复现 | Git, Jupyter, LaTeX | 编号化脚本、固定随机种子、结果表与研究报告 |

## 学术与竞赛

2025 年国家奖学金 · 全国大学生数学竞赛广东省一等奖 · 全国大学生市场调查与分析大赛广东赛区一等奖 · 全国大学生统计建模大赛广东省三等奖 · MathorCup 数学应用挑战赛国家级三等奖

正在参与高维生存数据特征筛选研究（GCor-SIS）；相关论文已进入返修阶段，并于 2026 年全国高校本科生统计论坛作报告。

---

<p align="center">
  <a href="https://yei1y.github.io">Portfolio</a> &nbsp;&middot;&nbsp;
  <a href="mailto:yeily_github@163.com">yeily_github@163.com</a> &nbsp;&middot;&nbsp;
  Guangzhou, China
</p>
