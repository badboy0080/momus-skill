from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "assets" / "use-cases"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

FONT_DIR = Path("C:/Windows/Fonts")
FONT_REGULAR = str(FONT_DIR / "msyh.ttc")
FONT_BOLD = str(FONT_DIR / "msyhbd.ttc")


CASES = [
    {
        "file": "software-bug-review.png",
        "title": "Use Case 01 / Software Bug",
        "tag": "software-development",
        "weak": "帮我修复登录接口报错",
        "critique": "这个 prompt 像把一张空白病历塞给外科医生，然后期待他顺手完成开颅。缺少错误信息、复现步骤、相关接口、期望行为和验证方式，继续执行只能靠 agent 猜。",
        "rewrite": [
            "请你作为资深后端工程师，先阅读当前仓库并定位登录接口相关代码。",
            "目标：修复登录接口报错，并保持改动最小。",
            "上下文：如果仓库中有测试、日志、路由、认证中间件或错误处理代码，请优先从这些线索定位问题。",
            "范围：只修改登录流程直接相关代码，不做无关重构。",
            "验证：补充或运行能覆盖该错误的测试；如果无法运行测试，请说明原因并给出手动验证步骤。",
            "输出：说明根因、修改内容和验证结果。",
        ],
        "question": "要不要采用这版，还是继续把 bug 当成玄学供 agent 占卜？",
    },
    {
        "file": "frontend-page-review.png",
        "title": "Use Case 02 / Frontend Page",
        "tag": "frontend-design",
        "weak": "帮我做一个好看的前端页面",
        "critique": "“好看”不是需求，是审美彩票。这里没有产品类型、目标用户、页面结构、视觉方向、交互状态或响应式验收标准，agent 只能生产一张泛用模板皮。",
        "rewrite": [
            "请你作为资深前端工程师和 UI 设计师，基于当前项目实现一个真实可用的首页。",
            "目标：完成首屏和核心内容区，让页面符合项目主题，而不是通用营销模板。",
            "范围：检查现有技术栈、样式系统和组件约定；只新增或修改实现该页面必要的文件。",
            "要求：包含清晰的信息层级、真实内容、响应式布局、按钮状态和可访问性基础。",
            "验证：启动本地页面，用桌面和移动视口截图检查无重叠、无溢出、主视觉正常渲染。",
            "输出：列出修改文件、设计取向和验证结果。",
        ],
        "question": "采用这版吧，还是继续用“好看”两个字召唤随机审美？",
    },
    {
        "file": "deployment-review.png",
        "title": "Use Case 03 / Deployment",
        "tag": "deployment-workflow",
        "weak": "帮我上线这个项目",
        "critique": "上线不是按一下宇宙按钮。你没说目标平台、环境变量、构建命令、测试门槛、回滚方式或生产验证，直接做等于把部署流程交给运气。",
        "rewrite": [
            "请你作为发布工程师，先检查当前仓库的部署配置、构建脚本和 README 中的运行说明。",
            "目标：将项目准备到可部署状态，并在明确平台后执行上线或给出上线步骤。",
            "范围：检查 package/build 配置、环境变量需求、部署平台配置和生产健康检查入口。",
            "要求：不要泄露密钥；不要执行破坏性发布操作；任何需要外部凭据的步骤先明确说明。",
            "验证：运行构建和相关测试；部署后检查生产 URL、控制台错误和关键页面状态。",
            "输出：给出执行过的命令、部署结果、生产验证和剩余风险。",
        ],
        "question": "要不要用这版上线计划，还是继续把生产环境当许愿池？",
    },
]


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REGULAR, size)


def wrap_text(text, max_chars):
    lines = []
    current = ""
    for char in text:
        if char == "\n":
            if current:
                lines.append(current)
                current = ""
            continue
        if len(current) >= max_chars:
            lines.append(current)
            current = ""
        current += char
    if current:
        lines.append(current)
    return lines


def draw_wrapped(draw, text, xy, max_chars, line_height, fill, text_font):
    x, y = xy
    for paragraph in text.split("\n"):
        for line in wrap_text(paragraph, max_chars):
            draw.text((x, y), line, font=text_font, fill=fill)
            y += line_height
        y += 4
    return y


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def render_case(case):
    image = Image.new("RGB", (1400, 880), "#080b12")
    draw = ImageDraw.Draw(image)

    for y in range(880):
        r = 8 + int(y * 0.010)
        g = 11 + int(y * 0.014)
        b = 18 + int(y * 0.026)
        draw.line([(0, y), (1400, y)], fill=(r, g, b))

    rounded(draw, (70, 52, 1330, 828), 28, "#0f172a", "#334155", 2)
    rounded(draw, (70, 52, 1330, 126), 28, "#111827", "#334155", 1)
    draw.rectangle((70, 96, 1330, 126), fill="#111827")
    rounded(draw, (104, 78, 140, 114), 10, "#22d3ee")
    draw.text((156, 80), case["title"], font=font(28, True), fill="#f8fafc")
    rounded(draw, (1030, 76, 1296, 116), 20, "#172554", "#2563eb", 1)
    draw.text((1052, 85), case["tag"], font=font(18, True), fill="#bfdbfe")

    rounded(draw, (104, 160, 504, 770), 20, "#020617", "#334155", 1)
    draw.text((134, 194), "WEAK PROMPT", font=font(18, True), fill="#94a3b8")
    rounded(draw, (134, 230, 474, 356), 18, "#3b1111", "#ef4444", 1)
    draw_wrapped(draw, case["weak"], (158, 268), 10, 38, "#fecaca", font(30, True))
    draw.text((134, 406), "MOMUS CRITIQUE", font=font(18, True), fill="#94a3b8")
    draw_wrapped(draw, case["critique"], (134, 444), 17, 34, "#dbeafe", font(21))

    rounded(draw, (528, 160, 1296, 770), 20, "#020617", "#334155", 1)
    draw.text((560, 194), "MOMUS REWRITE", font=font(34, True), fill="#f8fafc")
    rounded(draw, (560, 250, 1264, 642), 18, "#070b12", "#0e7490", 1)
    y = 280
    for index, line in enumerate(case["rewrite"]):
        fill = "#fde68a" if index == 0 else "#cbd5e1"
        y = draw_wrapped(draw, line, (590, y), 27, 30, fill, font(20))
        y += 2

    rounded(draw, (560, 672, 1264, 734), 16, "#431407", "#f97316", 1)
    draw_wrapped(draw, case["question"], (586, 690), 33, 30, "#fed7aa", font(21, True))

    image.save(OUTPUT_DIR / case["file"])


for item in CASES:
    render_case(item)

print(f"Rendered {len(CASES)} use case screenshots to {OUTPUT_DIR}")
