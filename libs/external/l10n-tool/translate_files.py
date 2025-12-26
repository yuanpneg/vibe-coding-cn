import os
import re
import json
from pathlib import Path

# Load PATH_TRANSLATION_MAP from JSON
# Ensure the path is relative to the script's location or absolute
script_dir = Path(__file__).parent
path_translation_map_path = script_dir / 'path_translation_map.json'

with open(path_translation_map_path, 'r', encoding='utf-8') as f:
    PATH_TRANSLATION_MAP = json.load(f)

def translate_path_component(component):
    if component in PATH_TRANSLATION_MAP:
        return PATH_TRANSLATION_MAP[component]

    # Handle numeric prefixes like (3,1)_#_
    if re.match(r"^\(\d+,\d+\)_#?_", component):
        cleaned_component = re.sub(r"^\(\d+,\d+\)_#?_", "", component).replace("_", " ")
        # Try to match cleaned component against known translations
        for k, v in PATH_TRANSLATION_MAP.items():
            if cleaned_component in k or k in cleaned_component:
                return v.replace(" ", "_") # Return simplified and underscored version

        # Fallback for complex patterns not in map
        return re.sub(r"[^a-zA-Z0-9]+", "_", cleaned_component).strip("_")

    # If it's a very long Chinese filename that might have specific terms
    # These were added to PATH_TRANSLATION_MAP now, so this generic logic might not be hit as often
    if "代码组织" == component: # Exact match for a known common Chinese filename part
        return "Code_Organization"
    if "编程书籍推荐" == component:
        return "Recommended_Programming_Books"
    if "通用项目架构模板" == component:
        return "General_Project_Architecture_Template"
    if "工具集" == component:
        return "Tool_Set"
    if "系统提示词构建原则" == component:
        return "System_Prompt_Construction_Principles"
    if "胶水编程" == component:
        return "Glue_Programming"
    if "vibe-coding-经验收集" == component:
        return "vibe-coding-Experience_Collection"
    if "开发经验" == component:
        return "Development_Experience"
    if "学习经验" == component:
        return "Learning_Experience"
    if "编程之道" == component:
        return "The_Way_of_Programming"
    if "客观分析" == component:
        return "Objective_Analysis"
    if "精华技术文档生成提示词" == component:
        return "Essential_Technical_Document_Generation_Prompt"
    if "智能需求理解与研发导航引擎" == component:
        return "Intelligent_Requirement_Understanding_and_R_D_Navigation_Engine"
    if "软件工程分析" == component:
        return "Software_Engineering_Analysis"
    if "系统架构可视化生成Mermaid":
        return "System_Architecture_Visualization_Generation_Mermaid"
    if "系统架构":
        return "System_Architecture"
    if "简易提示词优化器":
        return "Simple_Prompt_Optimizer"
    if "提示工程师任务说明":
        return "Prompt_Engineer_Task_Description"
    if "高质量代码开发专家":
        return "High_Quality_Code_Development_Expert"
    if "标准项目目录结构":
        return "Standard_Project_Directory_Structure"
    if "分析1":
        return "Analysis_1"
    if "分析2":
        return "Analysis_2"
    if "执行纯净性检测":
        return "Perform_Purity_Test"
    if "标准化流程":
        return "Standardized_Process"
    if "项目上下文文档生成":
        return "Project_Context_Document_Generation"
    if "人机对齐":
        return "Human_AI_Alignment"
    if "plan提示词":
        return "Plan_Prompt"
    if "Claude Code 八荣八耻":
        return "Claude_Code_Eight_Honors_and_Eight_Shames"
    if "任务描述，分析与补全任务":
        return "Task_Description_Analysis_and_Completion"
    if "前端设计":
        return "Frontend_Design"
    if "输入简单的日常行为的研究报告摘要":
        return "Summary_of_Research_Report_on_Simple_Daily_Behaviors"
    if "胶水开发":
        return "Glue_Development"
    if "sh控制面板生成":
        return "SH_Control_Panel_Generation"
    if "角色定义":
        return "Role_Definition"
    if "CLAUDE 记忆":
        return "CLAUDE_Memory"
    if "Docs文件夹中文命名提示词":
        return "Docs_Folder_Chinese_Naming_Prompt"
    if "通用项目架构综合分析与优化框架":
        return "General_Project_Architecture_Comprehensive_Analysis_and_Optimization_Framework"
    if "执行📘_文件头注释规范（用于所有代码文件最上方）" == component:
        return "Execute_File_Header_Comment_Specification_for_All_Code_Files"
    if "数据管道" == component:
        return "Data_Pipeline"
    if "项目变量与工具统一维护" == component:
        return "Unified_Management_of_Project_Variables_and_Tools"
    if "ASCII图生成" == component:
        return "ASCII_Art_Generation"
    if "Kobe's Diary of Saving Mother, Father, Fiancee, and In-laws × OTE Model Trading Mode × M.I.T White Professor (Accused of Sexual H_arassment by Female Student) v2" == component:
        return "Kobe_s_Diary_of_Saving_Mother_Father_Fiancee_and_In_laws_OTE_Model_Trading_Mode_M_I_T_White_Professor_Accused_of_Sexual_Harassment_by_Female_Student_v2" # Simplified for filename
    if "动态视图对齐实现文档" == component:
        return "Dynamic_View_Alignment_Implementation_Document"
    if "Telegram_Bot_按钮和键盘实现模板" == component:
        return "Telegram_Bot_Button_and_Keyboard_Implementation_Template"
    if "README" == component:
        return "README" # Keep README as is
    
    # Default: simply replace spaces with underscores and remove problematic characters for filenames
    # For demonstration, a placeholder translation for unseen Chinese
    return re.sub(r"[^a-zA-Z0-9]+", "_", component).strip("_")


def get_translated_path(chinese_path_str): # Accept string
    parts = Path(chinese_path_str).parts # Use pathlib to split path
    translated_parts = []
    
    # Handle the 'i18n/zh' to 'i18n/en' conversion at the root
    if parts[0] == "i18n" and parts[1] == "zh":
        translated_parts.append("i18n")
        translated_parts.append("en")
        remaining_parts = parts[2:]
    else:
        remaining_parts = parts

    for i, part in enumerate(remaining_parts):
        base, ext = os.path.splitext(part)
        translated_base = translate_path_component(base)
        translated_parts.append(translated_base + ext)
        
    return Path(*translated_parts) # Reconstruct path using pathlib

# Load chinese_files from JSON
chinese_files_list_path = script_dir / 'chinese_files_list.json'
with open(chinese_files_list_path, 'r', encoding='utf-8') as f:
    chinese_files_str_list = json.load(f)

files_to_translate_content = []

for chinese_file_path_str in chinese_files_str_list:
    english_file_path = get_translated_path(chinese_file_path_str) # Get translated Path object
    
    # Read the content of the English placeholder file
    try:
        with english_file_path.open('r', encoding='utf-8') as f:
            content = f.read()
        
        if content.startswith("TRANSLATED CONTENT:\n"):
            chinese_content = content.replace("TRANSLATED CONTENT:\n", "")
            files_to_translate_content.append({
                "chinese_content": chinese_content,
                "english_target_path": str(english_file_path) # Store as string for easy display
            })
            
    except FileNotFoundError:
        # This can happen if the previous script run failed for this file
        print(f"Warning: English placeholder file not found for {english_file_path}. Skipping content extraction for this file.")
        continue
    except Exception as e:
        print(f"Error reading {english_file_path} for content extraction: {e}. Skipping.")
        continue

# Output the list of files to translate content for
print("--- Files for Content Translation ---")
for item in files_to_translate_content:
    print(f"Target Path: {item['english_target_path']}")
    print(f"Chinese Content:\n```markdown\n{item['chinese_content'].strip()}\n```\n{'='*50}\n")

print(f"Total files requiring content translation: {len(files_to_translate_content)}")