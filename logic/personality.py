def generate_user_analysis(vector):
    analysis = []

    if vector[1] > 60:
        analysis.append("🔥 你具备强烈的进攻型人格。")

    if vector[2] > 60:
        analysis.append("🧱 你是团队中的稳定核心。")

    if vector[0] > 60:
        analysis.append("🧠 你拥有极高的决策意识。")

    if vector[3] > 60:
        analysis.append("🎯 你注重技术与细节。")

    if vector[4] > 60:
        analysis.append("🌟 你具备天然的影响力。")

    return analysis