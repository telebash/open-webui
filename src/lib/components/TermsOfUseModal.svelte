<script lang="ts">
import Modal from '$lib/components/common/Modal.svelte';
import { getContext } from 'svelte';
import type { Writable } from 'svelte/store';

interface I18nStore extends Writable<any> {
	t: (key: string) => string;
}

const i18n = getContext<I18nStore>('i18n');

export let show = false;
</script>

<Modal bind:show size="md">
	<div>
		<div class="flex justify-between dark:text-gray-100 px-5 pt-4 pb-2">
			<div class="text-lg font-medium self-center font-primary">
				{$i18n.t('Terms of Use')}
			</div>
			<button
				class="self-center"
				on:click={() => {
					show = false;
				}}
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					viewBox="0 0 20 20"
					fill="currentColor"
					class="w-5 h-5"
				>
					<path
						d="M6.28 5.22a.75.75 0 00-1.06 1.06L8.94 10l-3.72 3.72a.75.75 0 101.06 1.06L10 11.06l3.72 3.72a.75.75 0 101.06-1.06L11.06 10l3.72-3.72a.75.75 0 00-1.06-1.06L10 8.94 6.28 5.22z"
					/>
				</svg>
			</button>
		</div>

		<div class="px-5 pb-4 dark:text-gray-200">
			<div class="prose dark:prose-invert max-w-none">
				<h2>{$i18n.t('1. Acceptance of Terms')}</h2>
				<p>
					{$i18n.t('By accessing or using freepass.ai ("the Service"), you agree to comply with and be bound by these Terms of Use. If you do not agree with any part of these terms, please refrain from using the Service. We may update these Terms periodically, and your continued use signifies acceptance of any changes.')}
				</p>

				<h2>{$i18n.t('2. Eligibility')}</h2>
				<p>
					{$i18n.t('You must be at least the age of majority in your jurisdiction to use the Service. By using the Service, you represent and warrant that you meet this age requirement.')}
				</p>

				<h2>{$i18n.t('3. Use of the Service')}</h2>
				<p>
					{$i18n.t('freepass.ai provides access to advanced AI models such as OpenAI\'s GPT-4, Anthropic\'s Claude, and Google\'s Gemini without subscription fees or performance limits. Use the Service solely for lawful purposes and in accordance with these Terms.')}
				</p>

				<h2>{$i18n.t('4. Intellectual Property')}</h2>
				<p>
					{$i18n.t('• freepass.ai\'s Content: All content, features, and functionality on freepass.ai, including but not limited to text, graphics, logos, images, and software, are the exclusive property of freepass.ai or its licensors unless otherwise stated. You may not reproduce, distribute, modify, or create derivative works from any materials on the Service without explicit permission from freepass.ai.')}
				</p>
				<p>
					{$i18n.t('• User Content: Any content you generate, submit, or share through the Service ("User Content") remains your sole property. By using the Service, you grant freepass.ai a non-exclusive, royalty-free, worldwide, transferable license to use, reproduce, distribute, prepare derivative works of, and display your User Content solely for the purpose of providing and improving the Service.')}
				</p>

				<h2>{$i18n.t('5. User Content & Conduct')}</h2>
				<p>
					{$i18n.t('• Ownership: You retain full ownership of any User Content you create using the Service.')}
				</p>
				<p>
					{$i18n.t('• License to freepass.ai: As outlined above, by submitting User Content, you grant freepass.ai the necessary rights to operate and enhance the Service.')}
				</p>
				<p>
					{$i18n.t('• Prohibited Content: You agree not to generate or share content that is unlawful, harmful, offensive, infringing, or otherwise objectionable. freepass.ai reserves the right to remove or modify any User Content that violates these Terms at its discretion.')}
				</p>

				<h2>{$i18n.t('6. Data Collection and Use')}</h2>
				<p>
					{$i18n.t('While currently free, freepass.ai may collect and use your data, including for advertising and analytics purposes, as described in our Privacy Policy. By using the Service, you consent to such data collection and use.')}
				</p>

				<h2>{$i18n.t('7. Disclaimer of Warranties')}</h2>
				<p>
					{$i18n.t('The Service is provided "as is" and "as available" without any warranties of any kind, express or implied. freepass.ai does not guarantee that the Service will be uninterrupted, error-free, or free of harmful components.')}
				</p>

				<h2>{$i18n.t('8. Limitation of Liability')}</h2>
				<p>
					{$i18n.t('In no event shall freepass.ai or its affiliates be liable for any indirect, incidental, special, consequential, or punitive damages arising out of your use of or inability to use the Service, even if advised of the possibility of such damages.')}
				</p>

				<h2>{$i18n.t('9. Modifications to the Service')}</h2>
				<p>
					{$i18n.t('freepass.ai reserves the right to modify, suspend, or discontinue the Service at any time without prior notice.')}
				</p>

				<h2>{$i18n.t('10. Termination')}</h2>
				<p>
					{$i18n.t('We may terminate or suspend your access to the Service immediately, without prior notice or liability, for any reason, including if you breach these Terms.')}
				</p>

				<h2>{$i18n.t('11. Governing Law')}</h2>
				<p>
					{$i18n.t('These Terms are governed by and construed in accordance with the laws of [Your Jurisdiction], without regard to its conflict of law principles.')}
				</p>

				<h2>{$i18n.t('12. Contact Us')}</h2>
				<p>
					{$i18n.t('If you have any questions about these Terms of Use, please contact us at info@zaytoon.io.')}
				</p>
			</div>
		</div>
	</div>
</Modal>