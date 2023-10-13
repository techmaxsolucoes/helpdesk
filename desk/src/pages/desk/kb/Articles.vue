<template>
	<div class="flex flex-col">
		<ListManager
			ref="articleList"
			:options="{
				doctype: 'HD Article',
				order_by: 'modified DESC',
				limit: 20,
			}"
		>
			<template #body="{ manager }">
				<ListViewer
					:options="{
						fields: {
							title: {
								label: 'Título',
								width: '5',
								priority: 1,
							},
							category_name: {
								label: 'Categoria',
								width: '3',
								priority: 1,
							},
							status: {
								label: 'Status',
								width: '2',
								priority: 1,
							},
							views: {
								label: 'Visualizações',
								width: '1',
								priority: 3,
							},
							modified: {
								label: 'Modificado em',
								width: '1',
								priority: 2,
								align: 'right',
							},
						},
					}"
					class="h-[calc(100vh-6.5rem)] text-base"
					@add-item="
						() => {
							$router.push('/kb/articles/new');
						}
					"
				>
					<template #top-sub-section-1>
						<TabButtons
							v-model="activeTab"
							:buttons="[
								{ label: 'Artigos', active: true },
								{ label: 'Ver na Web' },
							]"
						/>
					</template>
					<template #bulk-actions="{ selectedItems }">
						<div class="flex flex-row space-x-2">
							<CategorySelector
								@selection="
									(category) => {
										$resources.moveArticlesToCategory
											.submit({
												articles: Object.keys(selectedItems),
												category: category.name,
											})
											.then(() => {
												manager.unselect();
											});
									}
								"
							>
								<template #selector-main="{ show }">
									<Button @click="show">Mover para</Button>
								</template>
							</CategorySelector>
							<Dropdown
								placement="right"
								:options="[
									{
										label: 'Rascunho',
										onClick: () => {
											$resources.setStatusForArticles
												.submit({
													articles: Object.keys(selectedItems),
													status: 'Draft',
												})
												.then(() => {
													manager.unselect();
												});
										},
									},
									{
										label: 'Publicado',
										onClick: () => {
											$resources.setStatusForArticles
												.submit({
													articles: Object.keys(selectedItems),
													status: 'Published',
												})
												.then(() => {
													manager.unselect();
												});
										},
									},
								]"
							>
								<template #default="{ toggleDropdown }">
									<Button
										:loading="$resources.setStatusForArticles.loading"
										icon-right="chevron-down"
										class="ml-2"
										@click="toggleDropdown"
									>
										Marcar como
									</Button>
								</template>
							</Dropdown>
							<!-- <Button @click="() => {}">Add to FAQ</Button> -->
							<Button
								@click="
									() => {
										$resources.deleteArticles
											.submit({
												articles: Object.keys(selectedItems),
											})
											.then(() => {
												manager.unselect();
												manager.reload();
											});
									}
								"
								>Deletar</Button
							>
						</div>
					</template>
					<template #field-title="{ value, row }">
						<RouterLink
							:to="{
								path: `/kb/articles/${row.name}`,
							}"
							class="cursor-pointer text-gray-600 hover:text-gray-900"
							>{{ value }}</RouterLink
						>
					</template>
					<template #field-status="{ value }">
						<div
							:class="
								value === 'Published' ? 'text-green-500' : 'text-gray-500'
							"
						>
							{{ value }}
						</div>
					</template>
					<template #field-views="{ value }">
						<div>{{ value }}</div>
					</template>
					<template #field-modified="{ value }">
						<div>
							{{ $dayjs.shortFormating($dayjs(value).fromNow(), false) }}
						</div>
					</template>
				</ListViewer>
			</template>
		</ListManager>
	</div>
</template>

<script>
import ListManager from "@/components/global/ListManager.vue";
import ListViewer from "@/components/global/ListViewer.vue";
import CategorySelector from "@/components/desk/kb/CategorySelector.vue";
import { Dropdown } from "frappe-ui";
import TabButtons from "@/components/global/TabButtons.vue";

export default {
	name: "Articles",
	components: {
		ListManager,
		ListViewer,
		CategorySelector,
		Dropdown,
		TabButtons,
	},
	props: {
		categoryId: {
			type: String,
			default: "",
		},
	},
	data() {
		return {
			activeTab: "Artigos",
		};
	},
	resources: {
		moveArticlesToCategory() {
			return {
				url: "helpdesk.api.kb.move_articles_to_category",
			}
		},
		setStatusForArticles() {
			return {
				url: "helpdesk.api.kb.set_status_for_articles",
			}
		},
		deleteArticles() {
			return {
				url: "helpdesk.api.kb.delete_articles",
			}
		},
		knowledgeBase() {
			if (this.activeTab == "Ver na web") {
				this.$router.push({ path: "/kb" })
			}
		},
	},
};
</script>
