
import os
from utils import main_keyboard, temper_keyboard, stomach_keyboard, injury_keyboard, arhythmia_keyboard, headache_keyboard

def greet_user(update, context):
     reply_markup=main_keyboard()
     update.message.reply_text(
         f"Здравствуй, пользователь! Это автоответчик помощник 'Скорая помощь', здесь можно получить базовую консультацию о своем состоянии здоровья",
            reply_markup=main_keyboard()
    )

def temperature(update, context):
    update.message.reply_text(
        f"Вы чувствуете что у вас температура? Измеряли ли вы температуру тела термометром?",
        reply_markup=temper_keyboard()
    )

def subfebril_temper(update, context):
    update.message.reply_text(
        f"У вас, возможно, легкое течение ОРВИ, при наличии боли в горле - полоскания горла раствором Фурациллина, соды, соли. При насморке - сосудосуживающие преператы в виде нозального спрея, капель. При боле в горле - таблетки для рассасывания с анестезирующим эффектом. Если вам нужен больничный лист, справка - нужно обратиться в поликлинику к вашему участковому терапевту/педиатру. Данные симптомы могут сохраняться до 5-7 дней. Если вы болеете больше недели - необходимо обратиться к врачу для исключения осложений.",
        reply_markup=main_keyboard()
    )

def hi_temper(update, context):
    update.message.reply_text(
        f"Для снижения температуры нужно принять жаропонижающие препараты (Парацетамол, ибуклин, нурофен, ацетилсалециловая кислота - точные дозировки для взрослого/ребенка есть в сопровождающей препараты инструкции.). Все что принимается в таблетках/сиропах начинает действие через 2 часа после приема внутырь, все что в свечах/иньекциях набирает эффект в течении часа. Помимо жаропонижающих препаратов необходимо обильное дробное питье и симптоматическое лечение - насморк, боли в горле, кашель. Также необходимо обратиться в поликлинику к вашему участковому терапевту/педиатру для назначения лечения. Если вы болеете больше недели - необходимо обратиться к врачу для исключения осложений.",
        reply_markup=main_keyboard()
    )
def talk_to_me(update, context):
    user_text = update.message.text 
    update.message.reply_text('Пожалуйста, взаимодействуйте со мной с помощью команды "/start" командами из меню, если вы себя плохо чувствуете - обратитесь в Скорую неотложную помощь по телефону с домашнего телефона "03", с мобильного "103" либо "112".')

def stomach_ache(update, context):
    update.message.reply_text(
        f"У вас появились боли в животе? Если эти боли появились внезапно, резкие, то необходимо обратиться в медицинское учереждение.",
        reply_markup=stomach_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def chronic_stomach_ache(update, context):
    update.message.reply_text(
        f"Боли, которые вас переодически беспокоят, связаные с приемом тяжелой пищи, жирной пищи, алкоголя требуют спазмолитики(ношпа и т.д.) , ферменты с едой(мезим, панкреатин и т.д.), диету и задящее питание. Все остальное требует незамедлительного обследования, нужно обращаться в медучереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def travma_keyboard(update, context):
    update.message.reply_text(
        f"Вы получили травму не так давно? Или вас беспокоят боли в коленях, спине и т.д? если факта травмы не было, вам нужно обратиться в поликнику к терапевту/хирургу/травматологу/неврологу.",
        reply_markup=injury_keyboard()
    )

def travma_krov(update, context):
    update.message.reply_text(
        f"Если травма не глубокая, слабое кроветениче - можно наложить давящую повязку, обратиться в городской травмпункт(на территории городской поликлиники №1). В случае сильного кровотечения, глубокой раны - вызвать СМП, наложить давящую повязку либо прижать место ранения. Если рана на конечности - придать конечности возвышеное положение.",
        reply_markup=main_keyboard()
    )

def travma(update, context):
    update.message.reply_text(
        f"Если травма вызвана падением, ушибом, растяжением и конечность самостоятельно двигается(то есть человек может поднять руку/ногу), косвенный признак отсутсвия перелома, можно обратиться в городской травмпункт для исключения перелома. Если имеется видемая деформация, нарушение подвижности конечности - вызов СМП.",
        reply_markup=main_keyboard()
    )

def heart_keyboard(update, context):
    update.message.reply_text(
        f"Вы чувствуете сердцебиение, нарушение ритма в работе сердца?.",
        reply_markup=arhythmia_keyboard()
    )

def arhythmia_acute(update, context):
    update.message.reply_text(
        f"У вас появилось чувство сердцебиения, не ровной работы сердца? Пропуски в работе сердца(замирание), это повод обратиться в медицинскую орагнизацию для регистрации ЭКГ с целью исключения патологии. Если ваше состояние не сопровождается снижением Аретериального давления, головокружением, слабостью то возможно обращение в поликлинику. Если состояние возникло экстренно, внезапно, сопровождается слабостью, потероей сознания, головокружением - вызов СМП.",
        reply_markup=main_keyboard()
    )

def arhythmia_chron(update, context):
    update.message.reply_text(
        f"У вас уже ранее было нарушение ритма, либо вам выставлена постоянная форма аритмии? Если при приеме назначеных лекарственных средств эффекта нет, то в таком случае необходимо обратиться в медучереждение(поликлиника, СМП).",
        reply_markup=main_keyboard()
    )

def headache_key(update, context):
    update.message.reply_text(
        f"Причин для головной боли очень много, она может возникать из-за синдрома интоксикации(при заболевании простудой, ОРВИ и прочее), при повышеном давлении, как реакция на метоусловия, стресс. Также есть мигренозные боли.",
        reply_markup=headache_keyboard()
    )

def headache_acute(update, context):
    update.message.reply_text(
        f"При сильной внезапной головной боли необходимо измерить артериальное давление, температуру, обратиться в соответсвующее меню при патологии. Если состояние в норме то можно принять обезболивающее - Анальгин(спазмалгон, баралгин), Нурофен(ибупрофен), Найз. Возможны противопоказания. Если эффекта от обезболивания нет - рекомендовано обратиться в поликлинику к невроллогу.",
        reply_markup=main_keyboard()
    )

def headache_chron(update, context):
    update.message.reply_text(
        f"Если у вас выставлен диазноз мигрень - то помогают лишь препараты назначеные неврологом, все остальное может частично помогать, но сам приступ мигрени снимают только специальные препараты.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )

def acute_stomach_ache(update, context):
    update.message.reply_text(
        f"Если боли появились в течении 2-3 часов после сомнительной еды - возможно отравление, несварение пищи. Если этот дискомфорт сопутствует жидкому стулу, тошнотой рвотой - нужно принимать антимикробные препараты(ципролет, энтерофурил и прочее), обильное дробное питье, сорбенты(активированный уголь, посиорб, энтеросгель и прочее). При ухудшении состояния - обратиться в медицинское учереждение.",
        reply_markup=main_keyboard()
    )
